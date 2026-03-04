#!/usr/bin/env python3
"""
frida-lint: Ruff-inspired linter and formatter for FRIDA (.txt) scripts.

Usage:
  python tools/frida_lint.py check <files|globs>
  python tools/frida_lint.py format <files|globs>

Stdlib only: re, argparse, json, dataclasses, pathlib, sys, difflib, glob.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Callable
from collections import Counter

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

READER_PREFIXES = (
    "SAP ", "Excel ", "Web ", "File ", "Titanium ", "Word ", "PPT ", "DB ",
    "Mail ", "SendMail ", "GetHome ", "GetCurrentDate ", "Message ", "Finish ",
    "RunScript ", "ApplyRegex ", "ReplaceFromVariable ", "Trim ", "CountItems ",
    "AddValueToList ", "AddVarToList ", "SplitIntoList ", "TrimList ",
    "RemoveDuplicatesInList ", "MathOperation ", "ApplyFilterInList ",
    "Get2DListItem ", "AddValueTo2DList ", "Substring ", "SystemNotify ",
    "systemnotify ",
)

NOQA_INLINE_RE = re.compile(r"\s*##\s+noqa(?::\s*([A-Z0-9,\s]+))?\s*$", re.IGNORECASE)
NOQA_BEGIN_RE = re.compile(r"^\s*##\s+noqa-begin(?::\s*([A-Z0-9,\s]+))?\s*$", re.IGNORECASE)
NOQA_END_RE = re.compile(r"^\s*##\s+noqa-end(?::\s*([A-Z0-9,\s]+))?\s*$", re.IGNORECASE)

# -----------------------------------------------------------------------------
# Config
# -----------------------------------------------------------------------------


@dataclass
class Config:
    indent: str = "tab"
    indent_size: int = 4
    select: list[str] = field(default_factory=lambda: ["ALL"])
    ignore: list[str] = field(default_factory=list)
    fixable: list[str] = field(default_factory=lambda: ["ALL"])
    unfixable: list[str] = field(default_factory=list)
    per_file_ignores: dict[str, list[str]] = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path | None = None) -> Config:
        if path is None:
            cwd = Path.cwd()
            for p in [cwd / ".fridalintrc", cwd / ".frida-lintrc"]:
                if p.exists():
                    path = p
                    break
        if path is None or not path.exists():
            return cls()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return cls()
        return cls(
            indent=data.get("indent", "tab"),
            indent_size=int(data.get("indent_size", 4)),
            select=data.get("select", ["ALL"]),
            ignore=data.get("ignore", []),
            fixable=data.get("fixable", ["ALL"]),
            unfixable=data.get("unfixable", []),
            per_file_ignores=data.get("per-file-ignores", data.get("per_file_ignores", {})),
        )

    def rule_enabled(self, code: str, file_name: str = "") -> bool:
        if not self._matches(code, self.select, default=True):
            return False
        if self._matches(code, self.ignore, default=False):
            return False
        if file_name and file_name in self.per_file_ignores:
            if self._matches(code, self.per_file_ignores[file_name], default=False):
                return False
        return True

    def fix_enabled(self, code: str) -> bool:
        if self._matches(code, self.unfixable, default=False):
            return False
        return self._matches(code, self.fixable, default=True)

    @staticmethod
    def _matches(code: str, patterns: list[str], default: bool) -> bool:
        if not patterns or (len(patterns) == 1 and patterns[0] == "ALL"):
            return default
        for p in patterns:
            if p == "ALL":
                return True
            if p in ("E", "W", "C", "S") and code and code[0] == p:
                return True
            if code == p:
                return True
        return False


# -----------------------------------------------------------------------------
# Line types and parse records
# -----------------------------------------------------------------------------


class LineType(Enum):
    block_open = "block_open"
    block_close = "block_close"
    region_open = "region_open"
    region_close = "region_close"
    comment = "comment"
    instruction = "instruction"
    variable_op = "variable_op"
    blank = "blank"


@dataclass
class LineRecord:
    line_no: int
    raw: str
    stripped: str
    line_type: LineType
    block_keyword: str
    depth: int
    noqa_codes: set[str] = field(default_factory=set)


@dataclass
class Diagnostic:
    file: str
    line: int
    col: int
    code: str
    message: str
    severity: str  # error, warning, convention, style
    fixable: bool = False
    fix_kind: str | None = None  # safe, unsafe
    fix_replacement: list[str] | None = None  # for --fix


# -----------------------------------------------------------------------------
# Noqa parsing
# -----------------------------------------------------------------------------


def parse_noqa_inline(stripped: str) -> set[str]:
    """Extract ## noqa: CODE1, CODE2 from end of line. Returns set of codes or {'ALL'}."""
    m = NOQA_INLINE_RE.search(stripped)
    if not m:
        return set()
    group = m.group(1)
    if not group or not group.strip():
        return {"ALL"}
    return {c.strip() for c in group.split(",") if c.strip()}


def parse_noqa_begin(stripped: str) -> set[str]:
    m = NOQA_BEGIN_RE.match(stripped)
    if not m:
        return set()
    group = m.group(1)
    if not group or not group.strip():
        return {"ALL"}
    return {c.strip() for c in group.split(",") if c.strip()}


def parse_noqa_end(stripped: str) -> set[str]:
    m = NOQA_END_RE.match(stripped)
    if not m:
        return set()
    group = m.group(1)
    if not group or not group.strip():
        return {"ALL"}
    return {c.strip() for c in group.split(",") if c.strip()}


# -----------------------------------------------------------------------------
# Pass 1: Parser (line classifier, block stack, region stack, variable tracker)
# -----------------------------------------------------------------------------

# Block openers: keyword -> expected closer
BLOCK_OPENERS = {
    "if": "end",
    "else": "end",
    "try": "end",
    "catch": "end",
    "case": "end",
    "default": "end",
    "for": "}",
    "foreach": "}",
    "while": "}",
    "switch": "}",
}

# Regex patterns for line classification
RE_BLANK = re.compile(r"^\s*$")
RE_REGION_OPEN = re.compile(r"^\s*#%region(\s|$)", re.IGNORECASE)
RE_REGION_CLOSE = re.compile(r"^\s*#%endregion\s*$", re.IGNORECASE)
RE_COMMENT = re.compile(r"^\s*(##|#\*|#\?|#!)", re.IGNORECASE)
RE_END = re.compile(r"^\s*end\s*$", re.IGNORECASE)
RE_CLOSE_BRACE = re.compile(r"^\s*\}\s*$")
RE_IF = re.compile(r"^\s*if\s*\(")
RE_ELSE = re.compile(r"^\s*else\s*$")
RE_TRY = re.compile(r"^\s*try\s*$")
RE_CATCH = re.compile(r"^\s*catch\b")
RE_FOR = re.compile(r"^\s*for\s+")
RE_FOREACH = re.compile(r"^\s*foreach\s+")
RE_WHILE = re.compile(r"^\s*while\s*\(")
RE_SWITCH = re.compile(r"^\s*switch\s*\(")
RE_CASE = re.compile(r"^\s*case\s+")
RE_DEFAULT = re.compile(r"^\s*default\s*:")

RE_DEFINE_VAR = re.compile(r'DefineVariable\s+(?:type\s+"[^"]+"\s+)?as\s+"([^"]+)"', re.IGNORECASE)
RE_SAVE_AS = re.compile(r'(?:and\s+)?save(?:_as|\s+as)\s+(?:["{])([^"}]+)(?:["}])', re.IGNORECASE)
RE_SAVE_AS_BARE = re.compile(r'(?:and\s+)?save(?:_as|\s+as)\s+([A-Za-z_][A-Za-z0-9_]*)', re.IGNORECASE)
RE_SAVE_VALUE_AS = re.compile(r'save\s+its\s+value\s+as\s+["{]([^"}]+)["}]', re.IGNORECASE)
RE_GETHOME_AS = re.compile(r'GetHome\s+as\s+"([^"]+)"', re.IGNORECASE)
RE_GETCURRENTDATE_SAVE = re.compile(r'GetCurrentDate\s+.*?\s+and\s+save\s+as\s+([A-Za-z_][A-Za-z0-9_]*)', re.IGNORECASE)
RE_FOREACH_VAR = re.compile(r"^\s*foreach\s+(\w+)\s+in\s+", re.IGNORECASE)
RE_RUNTIME_VAR = re.compile(r"<<<([^>]+)>>>")
# Match only true globals of the form <<name>>, not the inner part of <<<name>>>.
# Use lookbehind/lookahead to ensure exactly two angle brackets.
RE_GLOBAL_VAR = re.compile(r"(?<!<)<<([^<>]+)>>(?!>)")
RE_BRACE_VAR = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")
RE_GLOBAL_DOC = re.compile(r"^\s*##\s*<<([^>]+)>>")
RE_RUNSCRIPT = re.compile(r"^\s*RunScript\s+(\S+)", re.IGNORECASE)
RE_CATCH_AS = re.compile(r"^\s*catch\s+as\s+(\w+)", re.IGNORECASE)


def _block_stack_per_line(records: list[LineRecord]) -> list[list[str]]:
    """Return a list (one per record) of block-keyword stacks at that point."""
    stack: list[str] = []
    result: list[list[str]] = []
    for r in records:
        if r.line_type == LineType.block_open and r.block_keyword in BLOCK_OPENERS:
            if r.block_keyword in ("else", "catch", "case", "default"):
                if stack and BLOCK_OPENERS.get(stack[-1]) == "end":
                    stack.pop()
            stack.append(r.block_keyword)
        elif r.line_type == LineType.block_close:
            if stack:
                stack.pop()
        result.append(list(stack))
    return result


def classify_line(stripped: str) -> tuple[LineType, str]:
    if RE_BLANK.match(stripped):
        return LineType.blank, ""
    if RE_REGION_OPEN.match(stripped):
        return LineType.region_open, "region"
    if RE_REGION_CLOSE.match(stripped):
        return LineType.region_close, "endregion"
    if RE_END.match(stripped):
        return LineType.block_close, "end"
    if RE_CLOSE_BRACE.match(stripped):
        return LineType.block_close, "}"
    if RE_ELSE.match(stripped):
        return LineType.block_open, "else"
    if RE_CATCH.match(stripped):
        return LineType.block_open, "catch"
    if RE_IF.match(stripped):
        return LineType.block_open, "if"
    if RE_TRY.match(stripped):
        return LineType.block_open, "try"
    if RE_FOREACH.match(stripped):
        return LineType.block_open, "foreach"
    if RE_FOR.match(stripped):
        return LineType.block_open, "for"
    if RE_WHILE.match(stripped):
        return LineType.block_open, "while"
    if RE_SWITCH.match(stripped):
        return LineType.block_open, "switch"
    if RE_CASE.match(stripped):
        return LineType.block_open, "case"
    if RE_DEFAULT.match(stripped):
        return LineType.block_open, "default"
    if RE_COMMENT.match(stripped):
        return LineType.comment, ""
    # Instruction: starts with a known reader prefix
    for prefix in READER_PREFIXES:
        if stripped.lstrip().startswith(prefix):
            return LineType.instruction, ""
    # Variable ops: DefineVariable, AddValueToList, MathOperation, var++, etc.
    if re.search(r"DefineVariable|AddValueToList|AddVarToList|MathOperation|CountItems|ApplyRegex|ReplaceFromVariable|TrimList|RemoveDuplicatesInList|SplitIntoList", stripped, re.IGNORECASE):
        return LineType.variable_op, ""
    if re.match(r"^\s*[A-Za-z_][A-Za-z0-9_]*\s*\+\+", stripped):
        return LineType.variable_op, ""
    return LineType.instruction, ""  # fallback: treat as instruction


@dataclass
class ParseContext:
    """State accumulated during parsing of a FRIDA script."""
    # Stack of (keyword, line_no, expected_closer) for open blocks.
    block_stack: list[tuple[str, int, str]] = field(default_factory=list)
    # Line numbers where #%region blocks opened (for unmatched-region detection).
    region_stack: list[int] = field(default_factory=list)
    # Map of local variable name -> list of line numbers where it was defined.
    declared: dict[str, list[int]] = field(default_factory=lambda: {})
    # Map of local variable name -> list of line numbers where it was used.
    used: dict[str, list[int]] = field(default_factory=lambda: {})
    # Globals of the form <<Var>> seen anywhere in the script.
    globals_used: set[str] = field(default_factory=set)
    # Globals that are documented in the header comment block.
    globals_documented: set[str] = field(default_factory=set)
    # Names passed to RunScript so we can validate existence.
    run_scripts: list[str] = field(default_factory=list)
    # True while we are still in the top-of-file header doc region.
    in_header_doc: bool = True
    # Excel workbook state flags.
    excel_wb_opened: bool = False
    excel_wb_closed: bool = False
    # Variables that are targets of save-as operations (GetHome, GetCurrentDate, etc.).
    save_as_vars: set[str] = field(default_factory=set)
    # Loop iteration variables from foreach.
    loop_vars: set[str] = field(default_factory=set)


def parse_file(lines: list[str], path: Path) -> tuple[list[LineRecord], ParseContext]:
    records: list[LineRecord] = []
    ctx = ParseContext()
    noqa_block_stack: list[set[str]] = []
    non_comment_non_blank = 0

    for i, raw in enumerate(lines):
        line_no = i + 1
        stripped = raw.rstrip("\r\n")

        # Collect documented globals (## <<Var>>) regardless of line type.
        for m in RE_GLOBAL_DOC.finditer(stripped):
            ctx.globals_documented.add(m.group(1))

        line_type, block_kw = classify_line(stripped)
        noqa_inline = parse_noqa_inline(stripped)

        noqa_begin = parse_noqa_begin(stripped)
        if noqa_begin:
            noqa_block_stack.append(noqa_begin)
        noqa_end = parse_noqa_end(stripped)
        if noqa_end and noqa_block_stack:
            noqa_block_stack.pop()

        noqa_codes = noqa_inline or (noqa_block_stack[-1] if noqa_block_stack else set())

        depth = len(ctx.block_stack)
        if line_type == LineType.block_close:
            if block_kw == "end":
                if ctx.block_stack and ctx.block_stack[-1][2] == "end":
                    ctx.block_stack.pop()
                depth = len(ctx.block_stack)
            else:
                if ctx.block_stack and ctx.block_stack[-1][2] == "}":
                    ctx.block_stack.pop()
                depth = len(ctx.block_stack)

        if line_type == LineType.block_open and block_kw:
            if block_kw in ("else", "catch"):
                if ctx.block_stack and ctx.block_stack[-1][2] == "end":
                    ctx.block_stack.pop()
                depth = len(ctx.block_stack)
                ctx.block_stack.append((block_kw, line_no, BLOCK_OPENERS[block_kw]))
                if block_kw == "catch":
                    m = RE_CATCH_AS.match(stripped)
                    if m:
                        ctx.save_as_vars.add(m.group(1))
            elif block_kw in BLOCK_OPENERS:
                closer = BLOCK_OPENERS[block_kw]
                ctx.block_stack.append((block_kw, line_no, closer))
            if block_kw == "foreach":
                m = RE_FOREACH_VAR.match(stripped)
                if m:
                    ctx.loop_vars.add(m.group(1))

        if line_type == LineType.region_open:
            ctx.region_stack.append(line_no)
        elif line_type == LineType.region_close:
            if ctx.region_stack:
                ctx.region_stack.pop()

        if line_type == LineType.variable_op or line_type == LineType.instruction:
            if ctx.in_header_doc and non_comment_non_blank > 20:
                ctx.in_header_doc = False
            m = RE_DEFINE_VAR.search(stripped)
            if m:
                name = m.group(1)
                ctx.declared.setdefault(name, []).append(line_no)
            for m in RE_SAVE_AS.finditer(stripped):
                ctx.save_as_vars.add(m.group(1).strip())
            for m in RE_SAVE_AS_BARE.finditer(stripped):
                ctx.save_as_vars.add(m.group(1))
            for m in RE_SAVE_VALUE_AS.finditer(stripped):
                ctx.save_as_vars.add(m.group(1).strip())
            for m in RE_GETHOME_AS.finditer(stripped):
                ctx.save_as_vars.add(m.group(1))
            for m in RE_GETCURRENTDATE_SAVE.finditer(stripped):
                ctx.save_as_vars.add(m.group(1))
            if line_type == LineType.variable_op:
                for m in RE_FOREACH_VAR.finditer(stripped):
                    ctx.loop_vars.add(m.group(1))
            for m in RE_RUNTIME_VAR.finditer(stripped):
                ctx.used.setdefault(m.group(1), []).append(line_no)
            for m in RE_GLOBAL_VAR.finditer(stripped):
                g = m.group(1)
                ctx.globals_used.add(g)
                if ctx.in_header_doc:
                    ctx.globals_documented.add(g)
            if "LoadWBook" in stripped or "NewWB" in stripped:
                ctx.excel_wb_opened = True
            if "Save" in stripped and "close" in stripped.lower():
                ctx.excel_wb_closed = True
            if "Close" in stripped and "WB" in stripped:
                ctx.excel_wb_closed = True
            m = RE_RUNSCRIPT.match(stripped)
            if m:
                ctx.run_scripts.append(m.group(1).strip())

        if line_type != LineType.comment and line_type != LineType.blank:
            non_comment_non_blank += 1
            if ctx.in_header_doc and (RE_GLOBAL_DOC.match(stripped) or "GLOBAL" in stripped.upper()):
                pass
            elif ctx.in_header_doc and non_comment_non_blank <= 15:
                pass
            else:
                ctx.in_header_doc = False

        records.append(LineRecord(
            line_no=line_no,
            raw=raw,
            stripped=stripped,
            line_type=line_type,
            block_keyword=block_kw,
            depth=depth,
            noqa_codes=noqa_codes,
        ))

    return records, ctx


# -----------------------------------------------------------------------------
# File resolution (globs, RunScript)
# -----------------------------------------------------------------------------


def resolve_files(paths: list[str], follow_scripts: bool = False) -> list[Path]:
    seen: set[Path] = set()
    result: list[Path] = []
    cwd = Path.cwd()

    for p in paths:
        if p == ".":
            for f in cwd.glob("*.txt"):
                f = f.resolve()
                if f not in seen:
                    seen.add(f)
                    result.append(f)
            continue
        path = Path(p)
        if not path.is_absolute():
            path = cwd / path
        if "*" in p or "?" in p:
            for f in path.parent.glob(path.name):
                f = f.resolve()
                if f.suffix.lower() == ".txt" and f not in seen:
                    seen.add(f)
                    result.append(f)
        elif path.exists():
            path = path.resolve()
            if path not in seen:
                seen.add(path)
                result.append(path)

    return sorted(result)


# -----------------------------------------------------------------------------
# Lint rules (E001-E008, W001-W018, C001-C008, S001-S003)
# -----------------------------------------------------------------------------

def rule_e001_continue(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    """Flag use of 'continue', which does not exist in FRIDA."""
    out: list[Diagnostic] = []
    for r in records:
        if r.line_type != LineType.instruction and r.line_type != LineType.variable_op:
            continue
        if re.match(r"^\s*continue\s*$", r.stripped):
            if "E001" in r.noqa_codes or "ALL" in r.noqa_codes:
                continue
            out.append(Diagnostic(
                file="", line=r.line_no, col=1, code="E001",
                message="'continue' does not exist in FRIDA; use flag variable + conditional instead",
                severity="error", fixable=True, fix_kind="unsafe",
            ))
    return out


def rule_e002_bare_bool(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    """Detect bare booleans in if() conditions (must use string comparison)."""
    out: list[Diagnostic] = []
    bare = re.compile(r"if\s*\(\s*<<<([^>]+)>>>\s*\)")
    comparison_ops = {"-eq", "-ne", "-gt", "-lt", "-like", "-match"}
    for r in records:
        if r.line_type != LineType.block_open or r.block_keyword != "if":
            continue
        m = bare.search(r.stripped)
        if not m:
            continue
        if any(op in r.stripped for op in comparison_ops):
            continue
        if "E002" in r.noqa_codes or "ALL" in r.noqa_codes:
            continue
        var = m.group(1)
        fix = f'if ("<<<{var}>>>" -eq "true")'
        new_line = bare.sub(fix, r.stripped, count=1)
        out.append(Diagnostic(
            file="", line=r.line_no, col=1, code="E002",
            message="Bare boolean in if(); use string comparison e.g. -eq \"true\"",
            severity="error", fixable=True, fix_kind="safe",
            fix_replacement=[new_line],
        ))
    return out


def rule_e003_compound_while(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for r in records:
        if r.line_type != LineType.block_open or r.block_keyword != "while":
            continue
        if re.search(r"-AND|-OR|-NOT|-XOR", r.stripped, re.IGNORECASE):
            if "E003" in r.noqa_codes or "ALL" in r.noqa_codes:
                continue
            out.append(Diagnostic(
                file="", line=r.line_no, col=1, code="E003",
                message="Compound operators (-AND/-OR/-NOT/-XOR) not allowed in while; use if+break inside loop",
                severity="error", fixable=True, fix_kind="unsafe",
            ))
    return out


def rule_e004_wrong_closer(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    stack: list[tuple[str, int, str]] = []
    for r in records:
        if r.line_type == LineType.block_open and r.block_keyword in BLOCK_OPENERS:
            if r.block_keyword in ("else", "catch", "case", "default"):
                if stack and stack[-1][2] == "end":
                    stack.pop()
            stack.append((r.block_keyword, r.line_no, BLOCK_OPENERS[r.block_keyword]))
        elif r.line_type == LineType.block_close:
            if r.block_keyword == "end":
                if stack and stack[-1][2] != "end":
                    out.append(Diagnostic(
                        file="", line=r.line_no, col=1, code="E004",
                        message=f"Block mismatch: '{stack[-1][0]}' closed with 'end', expected '}}'",
                        severity="error",
                    ))
                    stack.pop()
                elif stack:
                    stack.pop()
            elif r.block_keyword == "}":
                if stack and stack[-1][2] != "}":
                    out.append(Diagnostic(
                        file="", line=r.line_no, col=1, code="E004",
                        message=f"Block mismatch: '{stack[-1][0]}' closed with '}}', expected 'end'",
                        severity="error",
                    ))
                    stack.pop()
                elif stack:
                    stack.pop()
    return out


def rule_e005_unbalanced(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    stack: list[tuple[str, int, str]] = []
    for r in records:
        if r.line_type == LineType.block_open and r.block_keyword in BLOCK_OPENERS:
            if r.block_keyword in ("else", "catch", "case", "default"):
                if stack and stack[-1][2] == "end":
                    stack.pop()
            stack.append((r.block_keyword, r.line_no, BLOCK_OPENERS[r.block_keyword]))
        elif r.line_type == LineType.block_close:
            if stack:
                stack.pop()
            else:
                out.append(Diagnostic(
                    file="", line=r.line_no, col=1, code="E005",
                    message="Extra block closer (no matching opener)",
                    severity="error",
                ))
    if stack:
        out.append(Diagnostic(
            file="", line=stack[-1][1], col=1, code="E005",
            message=f"Unclosed block '{stack[-1][0]}' (missing '{stack[-1][2]}')",
            severity="error",
        ))
    return out


def rule_e006_throw(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for r in records:
        if re.search(r"\bThrow\b", r.stripped, re.IGNORECASE):
            if "E006" in r.noqa_codes or "ALL" in r.noqa_codes:
                continue
            out.append(Diagnostic(
                file="", line=r.line_no, col=1, code="E006",
                message="Throw does not exist in FRIDA",
                severity="error", fixable=True, fix_kind="safe",
                fix_replacement=[f"## FIXME: Throw does not exist in FRIDA\n## {r.stripped}"],
            ))
    return out


def rule_e007_multiline_instruction(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    """Only flag when previous line looks incomplete (ends with comma or open quote)."""
    out: list[Diagnostic] = []
    for i, r in enumerate(records):
        if r.line_type != LineType.instruction:
            continue
        if i + 1 >= len(records):
            continue
        next_r = records[i + 1]
        if next_r.line_type == LineType.blank or next_r.line_type == LineType.comment:
            continue
        stripped = r.stripped.rstrip()
        if not any(stripped.startswith(p) or stripped.lstrip().startswith(p) for p in READER_PREFIXES):
            continue
        if any(next_r.stripped.lstrip().startswith(p) for p in READER_PREFIXES):
            continue
        if next_r.stripped.strip().startswith(("##", "#%", "end", "if ", "else", "try", "catch", "for ", "foreach ", "while ", "switch ", "case ", "default", "DefineVariable", "AddValueToList", "Excel ", "SAP ")):
            continue
        if not (stripped.endswith(",") or stripped.endswith("(") or (stripped.count('"') % 2 == 1)):
            continue
        if "E007" not in r.noqa_codes and "ALL" not in r.noqa_codes:
            out.append(Diagnostic(
                file="", line=next_r.line_no, col=1, code="E007",
                message="Instruction may be split across lines (FRIDA requires single-line instructions)",
                severity="error",
            ))
    return out


def rule_e008_runscript_missing(records: list[LineRecord], ctx: ParseContext, script_dir: Path) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for name in ctx.run_scripts:
        base = name if name.endswith(".txt") else f"{name}.txt"
        if not (script_dir / base).exists():
            for r in records:
                if f"RunScript {name}" in r.stripped or f"RunScript {base}" in r.stripped:
                    if "E008" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                        out.append(Diagnostic(
                            file="", line=r.line_no, col=1, code="E008",
                            message=f"RunScript references missing file: {base}",
                            severity="error",
                        ))
                    break
    return out


def rule_w001_used_undeclared(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    all_declared = set(ctx.declared) | ctx.save_as_vars | ctx.loop_vars | ctx.globals_used
    for var, line_nos in ctx.used.items():
        if "[" in var or "<<" in var or ">>>" in var:
            continue
        if var in all_declared:
            continue
        for line_no in line_nos:
            out.append(Diagnostic(
                file="", line=line_no, col=1, code="W001",
                message=f"Variable '<<<{var}>>>' used but never declared",
                severity="warning",
            ))
    return out


def rule_w002_unused(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for var, decl_lines in ctx.declared.items():
        if var in ctx.loop_vars or var in ctx.save_as_vars:
            continue
        if var in ctx.used:
            continue
        for line_no in decl_lines:
            out.append(Diagnostic(
                file="", line=line_no, col=1, code="W002",
                message=f"Variable '{var}' declared but never used",
                severity="warning",
            ))
    return out


def rule_w003_undocumented_global(records: list[LineRecord], ctx: ParseContext, c001_fired: bool) -> list[Diagnostic]:
    if c001_fired:
        return []
    out: list[Diagnostic] = []
    for g in ctx.globals_used:
        if g in ctx.globals_documented:
            continue
        for r in records:
            if f"<<{g}>>" in r.stripped:
                if "W003" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                    out.append(Diagnostic(
                        file="", line=r.line_no, col=1, code="W003",
                        message=f"Global '<<{g}>>' used but not documented in header block",
                        severity="warning",
                    ))
                break
    return out


def rule_w004_systemnotify(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for r in records:
        if re.search(r"systemnotify|SystemNotify", r.stripped, re.IGNORECASE):
            if "W004" in r.noqa_codes or "ALL" in r.noqa_codes:
                continue
            out.append(Diagnostic(
                file="", line=r.line_no, col=1, code="W004",
                message="systemnotify/SystemNotify used (avoid unless explicitly requested)",
                severity="warning", fixable=True, fix_kind="unsafe",
                fix_replacement=[f"## LINT-DISABLED: {r.stripped}"],
            ))
    return out


def rule_w005_finish_in_loop(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    stacks = _block_stack_per_line(records)
    for r, stack in zip(records, stacks):
        if "Finish " in r.stripped or re.match(r"^\s*Finish\s+", r.stripped):
            in_loop = any(kw in ("for", "foreach", "while") for kw in stack)
            if in_loop and ("W005" not in r.noqa_codes and "ALL" not in r.noqa_codes):
                out.append(Diagnostic(
                    file="", line=r.line_no, col=1, code="W005",
                    message="Finish inside loop; consider log-and-continue for row-level errors",
                    severity="warning",
                ))
    return out


def rule_w006_sap_outside_try(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    stacks = _block_stack_per_line(records)
    for r, stack in zip(records, stacks):
        if not r.stripped.strip().startswith("SAP "):
            continue
        in_loop = any(kw in ("for", "foreach", "while") for kw in stack)
        in_protected = any(kw in ("try", "catch") for kw in stack)
        if in_loop and not in_protected:
            if "W006" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                out.append(Diagnostic(
                    file="", line=r.line_no, col=1, code="W006",
                    message="SAP instruction inside loop but outside try/catch block",
                    severity="warning",
                ))
    return out


def rule_w007_excel_not_closed(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    if not ctx.excel_wb_opened or ctx.excel_wb_closed:
        return []
    for r in reversed(records):
        if "LoadWBook" in r.stripped or "NewWB" in r.stripped:
            return [Diagnostic(
                file="", line=r.line_no, col=1, code="W007",
                message="Excel workbook opened but never closed (use Excel Save WB and close or Excel Close WB)",
                severity="warning",
            )]
    return []


def rule_w008_sendmail_chars(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    # Map problematic punctuation to ASCII-safe equivalents.
    translation = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2015": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201C": '"',
        "\u201D": '"',
    }
    for r in records:
        if "SendMail" not in r.stripped and "sendmail" not in r.stripped.lower():
            continue
        original = r.stripped
        fixed = "".join(translation.get(ch, ch) for ch in original)
        if fixed != original:
            if "W008" in r.noqa_codes or "ALL" in r.noqa_codes:
                continue
            out.append(Diagnostic(
                file="", line=r.line_no, col=1, code="W008",
                message="Special characters in SendMail (use hyphen and straight quotes)",
                severity="warning", fixable=True, fix_kind="safe",
                fix_replacement=[fixed],
            ))
    return out


def rule_w009_no_closetrans_in_catch(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    stacks = _block_stack_per_line(records)
    i = 0
    while i < len(records):
        r = records[i]
        stack = stacks[i]
        if r.line_type == LineType.block_open and r.block_keyword == "catch":
            catch_start = r.line_no
            catch_depth = len(stack)
            in_loop_at_catch = any(kw in ("for", "foreach", "while") for kw in stack)
            catch_has_closetrans = False
            has_sap_instruction = False
            j = i + 1
            while j < len(records):
                if len(stacks[j]) < catch_depth:
                    break
                text = records[j].stripped
                if "CloseTrans" in text:
                    catch_has_closetrans = True
                if text.strip().startswith("SAP "):
                    has_sap_instruction = True
                j += 1
            # Only warn for catch blocks that are both inside a loop and handle
            # transactional SAP work. Small inner catches that only set flags or
            # strings (no SAP calls) are ignored.
            if in_loop_at_catch and has_sap_instruction and not catch_has_closetrans:
                if "W009" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                    out.append(Diagnostic(
                        file="", line=catch_start, col=1, code="W009",
                        message="Catch inside loop without SAP CloseTrans (transaction recovery)",
                        severity="warning",
                    ))
            i = j
        else:
            i += 1
    return out


def rule_w010_unmatched_region(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    stack: list[int] = []
    for r in records:
        if r.line_type == LineType.region_open:
            stack.append(r.line_no)
        elif r.line_type == LineType.region_close:
            if stack:
                stack.pop()
            else:
                # Extra #%endregion without opener – treat as unmatched region as well.
                out.append(Diagnostic(
                    file="", line=r.line_no, col=1, code="W010",
                    message="Unmatched #%endregion (no corresponding #%region)",
                    severity="warning",
                ))
    if stack:
        # Report the first unmatched opener.
        line_no = stack[0]
        out.append(Diagnostic(
            file="", line=line_no, col=1, code="W010",
            message="Unmatched #%region (missing #%endregion)",
            severity="warning",
        ))
    return out


def rule_w011_readcell_without_check(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for i, r in enumerate(records):
        if "Excel ReadCell" not in r.stripped and "Excel ReadCellText" not in r.stripped:
            continue
        for m in RE_SAVE_VALUE_AS.finditer(r.stripped):
            var = m.group(1).strip()
            for j in range(i + 1, min(i + 20, len(records))):
                if f"<<<{var}>>>" in records[j].stripped and "SAP " in records[j].stripped:
                    has_if_guard = any("if " in records[k].stripped for k in range(i + 1, j))
                    if not has_if_guard:
                        if "W011" not in records[j].noqa_codes and "ALL" not in records[j].noqa_codes:
                            out.append(Diagnostic(
                                file="", line=records[j].line_no, col=1, code="W011",
                                message="Excel ReadCell result used in SAP without prior empty-check",
                                severity="warning",
                            ))
                    break
    return out


def rule_w012_sendkey_without_status(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for i, r in enumerate(records):
        if r.line_type != LineType.instruction:
            continue
        if "SAP SendKey 0" not in r.stripped and "SendKey 0" not in r.stripped:
            continue
        has_status = False
        for j in range(i + 1, min(i + 5, len(records))):
            n = records[j].stripped
            if "GetStatusInfo" in n or "RunScript CheckSAPStatus" in n or "CheckSAPStatus" in n:
                has_status = True
                break
            if n.strip().startswith("SAP ") or n.strip().startswith("Excel ") or n.strip().startswith("if "):
                break
        if not has_status and "W012" not in r.noqa_codes and "ALL" not in r.noqa_codes:
            out.append(Diagnostic(
                file="", line=r.line_no, col=1, code="W012",
                message="SAP SendKey 0 without subsequent GetStatusInfo or RunScript CheckSAPStatus",
                severity="warning",
            ))
    return out


def rule_w013_empty_catch(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    i = 0
    while i < len(records):
        r = records[i]
        if r.line_type == LineType.block_open and r.block_keyword == "catch":
            catch_line = r.line_no
            j = i + 1
            content_lines = []
            while j < len(records):
                if records[j].line_type == LineType.block_close and records[j].block_keyword == "end":
                    break
                if records[j].line_type != LineType.blank and records[j].line_type != LineType.comment:
                    content_lines.append(records[j])
                j += 1
            if len(content_lines) <= 1 and any("catch" in x.stripped for x in content_lines):
                content_lines = []
            if not content_lines:
                # Allow the documented SAP CloseTrans recovery pattern:
                # try / SAP CloseTrans / catch / ## Ignore ...
                # If the preceding non-comment, non-blank line before catch
                # contains SAP CloseTrans, treat this as intentional and do
                # not warn.
                k = i - 1
                allow_empty = False
                while k >= 0:
                    prev = records[k]
                    if prev.line_type in (LineType.blank, LineType.comment):
                        k -= 1
                        continue
                    if "SAP CloseTrans" in prev.stripped:
                        allow_empty = True
                    break
                if not allow_empty and "W013" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                    out.append(Diagnostic(
                        file="", line=catch_line, col=1, code="W013",
                        message="try block with empty catch (silently swallowing errors)",
                        severity="warning",
                    ))
            i = j
        i += 1
    return out


def rule_w018_for_zero_times(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for r in records:
        if r.line_type == LineType.block_open and r.block_keyword == "for":
            if re.search(r"for\s+0\s+times", r.stripped, re.IGNORECASE):
                if "W018" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                    out.append(Diagnostic(
                        file="", line=r.line_no, col=1, code="W018",
                        message="for 0 times - dead code, loop body never executes",
                        severity="warning", fixable=True, fix_kind="unsafe",
                    ))
    return out


def rule_c002_region_without_name(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for r in records:
        if r.line_type == LineType.region_open:
            name_part = r.stripped.replace("#%region", "").strip()
            if not name_part or name_part.strip() in ("-", "─", " "):
                if "C002" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                    out.append(Diagnostic(
                        file="", line=r.line_no, col=1, code="C002",
                        message="#%region without descriptive name",
                        severity="convention",
                    ))
    return out


def rule_c003_large_block_without_region(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    return []


def rule_s001_indentation(records: list[LineRecord], ctx: ParseContext, indent_str: str) -> list[Diagnostic]:
    out: list[Diagnostic] = []

    def leading_indent_level(raw: str) -> int:
        if indent_str == "	":
            return len(raw) - len(raw.lstrip("	"))
        level = 0
        i = 0
        step = len(indent_str)
        while raw[i:i + step] == indent_str:
            level += 1
            i += step
        return level

    for r in records:
        if r.line_type in (LineType.blank, LineType.comment, LineType.region_open, LineType.region_close):
            continue
        leading = r.raw[: len(r.raw) - len(r.raw.lstrip())]
        actual_level = leading_indent_level(leading)
        expected_level = r.depth

        if actual_level == expected_level:
            continue

        if not r.stripped or "S001" in r.noqa_codes or "ALL" in r.noqa_codes:
            continue

        out.append(Diagnostic(
            file="", line=r.line_no, col=1, code="S001",
            message=f"Expected indent level {expected_level}, found {actual_level}",
            severity="style", fixable=True, fix_kind="safe",
            fix_replacement=[(indent_str * expected_level) + r.stripped.lstrip()],
        ))
    return out


def rule_s002_comment_space(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for r in records:
        content = r.stripped.lstrip()
        if not content.startswith("##"):
            continue
        if content.startswith(("#%", "#*", "#?", "#!")):
            continue
        if re.match(r"^##[A-Za-z0-9<]", content):
            fixed = re.sub(r"^(##)([A-Za-z0-9<])", r"\1 \2", content, count=1)
            if "S002" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                out.append(Diagnostic(
                    file="", line=r.line_no, col=1, code="S002",
                    message="Comment missing space after ##",
                    severity="style", fixable=True, fix_kind="safe",
                    fix_replacement=[fixed],
                ))
    return out


def rule_s003_trailing_whitespace(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for r in records:
        if r.raw.rstrip("\r\n") != r.raw.rstrip():
            if "S003" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                out.append(Diagnostic(
                    file="", line=r.line_no, col=1, code="S003",
                    message="Trailing whitespace",
                    severity="style", fixable=True, fix_kind="safe",
                    fix_replacement=[r.stripped],
                ))
    return out


def rule_c001_missing_globals_doc(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    # If there are no globals, or all used globals are already documented, or a header
    # block already exists, do not generate a new header.
    if not ctx.globals_used or ctx.globals_documented >= ctx.globals_used:
        return []
    header_present = False
    for r in records:
        if r.line_type == LineType.comment and "GLOBAL VARIABLES" in r.stripped.upper():
            header_present = True
            break
    if header_present:
        return []
    block = [
        "## ─────────────────────────────────────────────────────────────────────────────",
        "## GLOBAL VARIABLES (define in Frida UI before execution)",
        "## ─────────────────────────────────────────────────────────────────────────────",
    ]
    for g in sorted(ctx.globals_used):
        block.append(f"## <<{g}>> - (define in UI)")
    block.append("## ─────────────────────────────────────────────────────────────────────────────")
    insert_line = 1
    for i, r in enumerate(records):
        if r.stripped.strip().startswith("GetHome") or r.stripped.strip().startswith("DefineVariable") or r.stripped.strip().startswith("Excel ") or r.stripped.strip().startswith("#%region"):
            insert_line = r.line_no
            break
    return [Diagnostic(
        file="", line=insert_line, col=1, code="C001",
        message="Missing global variables documentation block at script top",
        severity="convention", fixable=True, fix_kind="safe",
        fix_replacement=block,
    )]


def rule_c004_checkpoint_before_start_transaction(records: list[LineRecord], ctx: ParseContext) -> list[Diagnostic]:
    out: list[Diagnostic] = []
    for i, r in enumerate(records):
        m = re.search(r"SAP\s+StartTransaction\s+(\S+)", r.stripped, re.IGNORECASE)
        if not m:
            continue
        tcode = m.group(1)
        prev_comment = False
        for j in range(i - 1, max(-1, i - 5), -1):
            if records[j].line_type == LineType.comment and records[j].stripped.strip().startswith("##"):
                prev_comment = True
                break
            if records[j].line_type != LineType.blank and records[j].line_type != LineType.comment:
                break
        if not prev_comment:
            if "C004" not in r.noqa_codes and "ALL" not in r.noqa_codes:
                out.append(Diagnostic(
                    file="", line=r.line_no, col=1, code="C004",
                    message="No checkpoint comment before SAP StartTransaction",
                    severity="convention", fixable=True, fix_kind="safe",
                    fix_replacement=[f"## Start transaction {tcode}"],
                ))
    return out


def run_lint(records: list[LineRecord], ctx: ParseContext, config: Config, file_path: Path, indent_str: str) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    c001_fired = False

    def run_rule(code: str, fn: Callable[[], list[Diagnostic]]) -> list[Diagnostic]:
        diags = fn()
        for d in diags:
            d.file = str(file_path)
        return diags

    diags_c001 = run_rule("C001", lambda: rule_c001_missing_globals_doc(records, ctx))
    if diags_c001:
        c001_fired = True
    diagnostics.extend(diags_c001)

    rule_list: list[tuple[str, Callable[[], list[Diagnostic]]]] = [
        ("E001", lambda: rule_e001_continue(records, ctx)),
        ("E002", lambda: rule_e002_bare_bool(records, ctx)),
        ("E003", lambda: rule_e003_compound_while(records, ctx)),
        ("E004", lambda: rule_e004_wrong_closer(records, ctx)),
        ("E005", lambda: rule_e005_unbalanced(records, ctx)),
        ("E006", lambda: rule_e006_throw(records, ctx)),
        ("E007", lambda: rule_e007_multiline_instruction(records, ctx)),
        ("E008", lambda: rule_e008_runscript_missing(records, ctx, file_path.parent)),
        ("W001", lambda: rule_w001_used_undeclared(records, ctx)),
        ("W002", lambda: rule_w002_unused(records, ctx)),
        ("W003", lambda: rule_w003_undocumented_global(records, ctx, c001_fired)),
        ("W004", lambda: rule_w004_systemnotify(records, ctx)),
        ("W005", lambda: rule_w005_finish_in_loop(records, ctx)),
        ("W006", lambda: rule_w006_sap_outside_try(records, ctx)),
        ("W007", lambda: rule_w007_excel_not_closed(records, ctx)),
        ("W008", lambda: rule_w008_sendmail_chars(records, ctx)),
        ("W009", lambda: rule_w009_no_closetrans_in_catch(records, ctx)),
        ("W010", lambda: rule_w010_unmatched_region(records, ctx)),
        ("W011", lambda: rule_w011_readcell_without_check(records, ctx)),
        ("W012", lambda: rule_w012_sendkey_without_status(records, ctx)),
        ("W013", lambda: rule_w013_empty_catch(records, ctx)),
        ("W018", lambda: rule_w018_for_zero_times(records, ctx)),
        ("S001", lambda: rule_s001_indentation(records, ctx, indent_str)),
        ("S002", lambda: rule_s002_comment_space(records, ctx)),
        ("S003", lambda: rule_s003_trailing_whitespace(records, ctx)),
        ("C002", lambda: rule_c002_region_without_name(records, ctx)),
        ("C004", lambda: rule_c004_checkpoint_before_start_transaction(records, ctx)),
    ]
    for code, fn in rule_list:
        if not config.rule_enabled(code, file_path.name):
            continue
        for d in run_rule(code, fn):
            line_no = d.line
            noqa_codes = set()
            for r in records:
                if r.line_no == line_no:
                    noqa_codes = r.noqa_codes
                    break
            if "ALL" in noqa_codes or d.code in noqa_codes:
                continue
            diagnostics.append(d)

    return diagnostics


# -----------------------------------------------------------------------------
# Formatter (Pass 3)
# -----------------------------------------------------------------------------


def format_file(records: list[LineRecord], config: Config, preserve_tab_depth: bool = False) -> list[str]:
    indent_char = "\t" if config.indent == "tab" else " "
    indent_size = 1 if config.indent == "tab" else config.indent_size
    indent_str = indent_char * indent_size
    out: list[str] = []
    prev_blank = False
    for r in records:
        stripped = r.stripped
        content = stripped.lstrip()
        if r.line_type == LineType.blank:
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        prev_blank = False
        if preserve_tab_depth:
            existing_indent = r.stripped[: len(r.stripped) - len(r.stripped.lstrip())]
            out.append(existing_indent + content)
        else:
            # Canonical indentation is derived from control-flow depth.
            line_indent = indent_str * r.depth
            out.append(line_indent + content)
    result = "\n".join(out)
    if result and not result.endswith("\n"):
        result += "\n"
    return result.splitlines(keepends=True) if result else []


def apply_fixes(lines: list[str], records: list[LineRecord], diagnostics: list[Diagnostic], config: Config, safe_only: bool) -> list[str]:
    """
    Apply fixes in a deterministic, bottom-up way without index drift.

    Strategy:
    - Compute patch operations against the original line numbers.
    - Sort operations by (line, op_type) descending and apply to a working copy.
    """
    # Collect patch operations.
    ops: list[tuple[int, str, list[str], str]] = []  # (line_index, op_type, payload_lines, code)

    for d in diagnostics:
        if not d.fixable or not d.fix_replacement:
            continue
        if safe_only and d.fix_kind == "unsafe":
            continue
        if not config.fix_enabled(d.code):
            continue
        line_idx = max(0, d.line - 1)  # 0-based index

        # C001: insert header block before first non-header instruction.
        if d.code == "C001":
            payload = [ln.rstrip("\n") + "\n" for ln in d.fix_replacement]
            ops.append((max(0, d.line - 1), "insert_before", payload, d.code))
            continue

        # E006: might expand into two lines.
        if d.code == "E006":
            rep = d.fix_replacement[0]
            if "\n" in rep:
                a, b = rep.split("\n", 1)
                payload = [a + "\n", b + "\n"]
                ops.append((line_idx, "replace_two", payload, d.code))
            else:
                payload = [rep.rstrip("\n") + "\n"]
                ops.append((line_idx, "replace_one", payload, d.code))
            continue

        # C004: insert checkpoint comment immediately before StartTransaction line.
        if d.code == "C004":
            payload = [d.fix_replacement[0].rstrip("\n") + "\n"]
            ops.append((line_idx, "insert_before", payload, d.code))
            continue

        # Default: single-line replacement.
        if len(d.fix_replacement) == 1:
            payload = [d.fix_replacement[0].rstrip("\n") + "\n"]
            ops.append((line_idx, "replace_one", payload, d.code))

    if not ops:
        return lines

    # Normalize lines to always end with a newline to simplify replacements.
    fixed_lines = [ln if ln.endswith("\n") else ln + "\n" for ln in lines]

    # Sort operations bottom-up so earlier indices are unaffected by later inserts.
    order = {"insert_block_top": 0, "insert_before": 1, "replace_two": 2, "replace_one": 3}
    ops.sort(key=lambda t: (t[0], order.get(t[1], 99)), reverse=True)

    for line_idx, op_type, payload, code in ops:
        if op_type == "insert_block_top":
            fixed_lines = payload + fixed_lines
            continue
        if line_idx < 0 or line_idx >= len(fixed_lines):
            continue
        if op_type == "insert_before":
            fixed_lines[line_idx:line_idx] = payload
        elif op_type == "replace_two":
            # Replace the target line and insert the second immediately after.
            fixed_lines[line_idx:line_idx + 1] = payload
        elif op_type == "replace_one":
            fixed_lines[line_idx:line_idx + 1] = payload

    return fixed_lines


# -----------------------------------------------------------------------------
# Output
# -----------------------------------------------------------------------------

def output_terminal(diagnostics: list[Diagnostic], color: bool = True) -> None:
    red = "\033[31m" if color else ""
    yellow = "\033[33m" if color else ""
    blue = "\033[34m" if color else ""
    dim = "\033[2m" if color else ""
    reset = "\033[0m" if color else ""
    for d in diagnostics:
        severity_color = red if d.severity == "error" else yellow if d.severity == "warning" else blue if d.severity == "convention" else dim
        fix_tag = f" [{d.fix_kind or 'safe'} fix]" if d.fixable else ""
        print(f"{d.file}:{d.line}:1: {severity_color}{d.code}{reset} {d.message}{fix_tag}")
    errors = sum(1 for d in diagnostics if d.severity == "error")
    warnings = sum(1 for d in diagnostics if d.severity == "warning")
    conventions = sum(1 for d in diagnostics if d.severity == "convention")
    style = sum(1 for d in diagnostics if d.severity == "style")
    fixable_safe = sum(1 for d in diagnostics if d.fixable and d.fix_kind == "safe")
    fixable_unsafe = sum(1 for d in diagnostics if d.fixable and d.fix_kind == "unsafe")
    print()
    print(f"Found {len(diagnostics)} issues ({errors} errors, {warnings} warnings, {conventions} conventions, {style} style)")
    if fixable_safe or fixable_unsafe:
        print(f"{fixable_safe} fixable with --fix, {fixable_unsafe} additionally fixable with --unsafe-fixes")


def output_json(diagnostics: list[Diagnostic]) -> None:
    arr = []
    for d in diagnostics:
        arr.append({
            "file": d.file,
            "line": d.line,
            "col": d.col,
            "code": d.code,
            "message": d.message,
            "severity": d.severity,
            "fixable": d.fixable,
            "fix_kind": d.fix_kind,
        })
    print(json.dumps(arr, indent=2))


def output_statistics(diagnostics: list[Diagnostic]) -> None:
    counts: Counter[str] = Counter()
    for d in diagnostics:
        counts[d.code] += 1
    for code in sorted(counts.keys()):
        n = counts[code]
        d0 = next(d for d in diagnostics if d.code == code)
        fix_tag = f" ({d0.fix_kind or 'safe'} fix)" if d0.fixable else ""
        print(f"{code}  {n}  {d0.message}{fix_tag}")


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(prog="frida-lint", description="Lint and format FRIDA .txt scripts")
    parser.add_argument("--config", type=Path, default=None, help="Path to .fridalintrc")
    parser.add_argument("--no-color", action="store_true", help="Disable colored output")
    parser.add_argument("--follow-scripts", action="store_true", help="Also lint files referenced by RunScript")
    sub = parser.add_subparsers(dest="command", required=True)

    check_parser = sub.add_parser("check", help="Lint and optionally fix")
    check_parser.add_argument("files", nargs="+", help="Files or globs (e.g. *.txt)")
    check_parser.add_argument("--fix", action="store_true", help="Apply safe fixes")
    check_parser.add_argument("--unsafe-fixes", action="store_true", help="Apply unsafe fixes too")
    check_parser.add_argument("--diff", action="store_true", help="Show diff of fixes, don't write")
    check_parser.add_argument("--statistics", action="store_true", help="Show rule statistics")
    check_parser.add_argument("--json", action="store_true", help="JSON output")
    check_parser.add_argument("--select", type=str, default="", help="Comma-separated rules to enable")
    check_parser.add_argument("--ignore", type=str, default="", help="Comma-separated rules to ignore")
    check_parser.add_argument("--safe-tabs", action="store_true", help="Preserve existing tab depth and disable S001 fixes/reports")

    format_parser = sub.add_parser("format", help="Format files")
    format_parser.add_argument("files", nargs="+", help="Files or globs")
    format_parser.add_argument("--diff", action="store_true", help="Show diff only")
    format_parser.add_argument("--check", action="store_true", help="Exit 1 if would reformat")
    format_parser.add_argument("--safe-tabs", action="store_true", help="Preserve existing tab depth (avoid parser-depth reindent)")

    args = parser.parse_args()
    config = Config.load(args.config)
    if getattr(args, "select", None) and args.select:
        config.select = [s.strip() for s in args.select.split(",")]
    if getattr(args, "ignore", None) and args.ignore:
        config.ignore = [s.strip() for s in args.ignore.split(",")]

    paths = resolve_files(getattr(args, "files", []), follow_scripts=getattr(args, "follow_scripts", False))
    if not paths:
        print("No .txt files found", file=sys.stderr)
        return 1

    indent_str = "\t" if config.indent == "tab" else " " * config.indent_size

    if args.command == "check":
        all_diagnostics: list[Diagnostic] = []
        for path in paths:
            text = path.read_text(encoding="utf-8", errors="replace")
            lines = text.splitlines(keepends=True)
            if not lines:
                lines = [""]
            records, ctx = parse_file([line.rstrip("\r\n") for line in lines], path)
            diags = run_lint(records, ctx, config, path, indent_str)
            if getattr(args, "safe_tabs", False):
                diags = [d for d in diags if d.code != "S001"]
            all_diagnostics.extend(diags)
            if (args.fix or args.unsafe_fixes) and diags:
                safe_only = not args.unsafe_fixes
                fixed_lines = apply_fixes(lines, records, diags, config, safe_only=safe_only)
                if args.diff:
                    from io import StringIO
                    orig = "".join(lines)
                    new = "".join(fixed_lines) if isinstance(fixed_lines[0], str) else "".join(fixed_lines)
                    sys.stdout.writelines(difflib.unified_diff(orig.splitlines(keepends=True), new.splitlines(keepends=True), fromfile=str(path), tofile=str(path)))
                else:
                    path.write_text("".join(fixed_lines), encoding="utf-8")
        if args.json:
            output_json(all_diagnostics)
        elif args.statistics:
            output_statistics(all_diagnostics)
        else:
            output_terminal(all_diagnostics, color=not args.no_color)
        return 1 if all_diagnostics else 0

    if args.command == "format":
        changed = False
        for path in paths:
            text = path.read_text(encoding="utf-8", errors="replace")
            lines = text.splitlines(keepends=True)
            if not lines:
                lines = [""]
            records, _ = parse_file([line.rstrip("\r\n") for line in lines], path)
            formatted = format_file(records, config, preserve_tab_depth=getattr(args, "safe_tabs", False))
            new_text = "".join(formatted) if formatted else ""
            orig_text = "".join(lines)
            if new_text != orig_text:
                changed = True
                if args.diff:
                    sys.stdout.writelines(difflib.unified_diff(orig_text.splitlines(keepends=True), new_text.splitlines(keepends=True), fromfile=str(path), tofile=str(path)))
                elif not args.check:
                    path.write_text(new_text, encoding="utf-8")
        return 1 if (args.check and changed) else 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
