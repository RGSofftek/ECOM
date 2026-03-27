# FRIDA Lint Fix (iterative format → lint → propose → approve → fix)

Run the FRIDA formatter, then the linter; for any reported issues, propose solutions in chat, wait for approval, implement the approved fixes, and re-run until lint is clean.

## Target files

- If the user typed a path or glob after the command (e.g. `Actions.txt` or `*.txt`), use that as `<target>`.
- Otherwise: use the currently focused/active file if it is a `.txt` FRIDA script; if not, use `*.txt` in the project root.
- Run all commands from the project root so paths resolve correctly (e.g. on Windows: `c:\Users\...\ECOM`).

## Workflow (repeat until lint clean or max 10 iterations)

### Step 1 – Format then lint

1. Run: `python .cursor/tools/frida_lint.py format <target>`
2. Run: `python .cursor/tools/frida_lint.py check --json <target>` and capture full stdout and the exit code.

### Step 2 – If check reported issues (exit code 1)

1. Parse the JSON array of diagnostics. Each item has: `file`, `line`, `code`, `message`, `severity`, `fixable`, `fix_kind`.
2. For each diagnostic, present in chat:
   - **Location**: `file:line`
   - **Code**: `code`
   - **Message**: `message`
   - **Severity**: `severity`
   - **Proposed solution**:
     - If the rule is fixable by the linter (e.g. E002, S001, S002, S003, W008, C001, C004): describe the exact edit, or state that you will apply the linter’s safe/unsafe fix for this rule after approval.
     - If not fixable by the linter: propose a concrete code change (snippet or line-level edit).
3. Ask the user in chat: **"Approve all, approve specific items (by file:line or by code), or give feedback/changes."**
4. **Do not apply any file changes until the user has approved (all or a subset) in chat.**

### Step 3 – Apply approved fixes and re-run

1. After the user approves (all or a subset):
   - For approved diagnostics that are fixable by the linter: you may run `python .cursor/tools/frida_lint.py check --fix <target>` (and `--unsafe-fixes` only if the user explicitly allowed unsafe fixes) to apply those fixes in one go.
   - For all other approved diagnostics: implement the proposed edits in the workspace (apply the exact line/snippet changes you described).
2. Run again: `python .cursor/tools/frida_lint.py format <target>` then `python .cursor/tools/frida_lint.py check --json <target>`.
3. If the check still reports issues, go back to Step 2 (propose solutions → wait for approval → implement → re-run).
4. If the check passes (exit code 0), report **"Lint clean"** and stop.

### Step 4 – Loop and safety

- Repeat the cycle (format → check → propose → wait for approval → implement → format → check) until there are no diagnostics or until you have completed 10 iterations.
- If after 10 iterations there are still issues, report the remaining diagnostics and stop.

## Optional: using the linter’s built-in fix

- When the user approves "all" and every remaining diagnostic is fixable by the linter, you may run once: `python .cursor/tools/frida_lint.py check --fix <target>` (and `--unsafe-fixes` only if the user explicitly allows it).
- Then run `format` and `check --json` again and continue the propose/approve loop for any remaining (non-fixable or not-yet-approved) issues.

## Summary

- Prefer describing the exact line/change when proposing fixes; for fixable rules you may offer to run the linter with `--fix` (and `--unsafe-fixes` when approved) for approved items.
- Never apply file changes before the user has approved in chat.
