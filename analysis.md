# FRIDA Rules Compliance Analysis

**Script:** `Actions.txt`  
**Date:** 2026-02-26  
**Scope:** SAP Bot (Batch + Resumable) for Deal Contract creation

---

## Executive Summary

| Rule File | Status | Notes |
|-----------|--------|-------|
| frida-core.mdc | **COMPLIANT** | All syntax and structure rules followed |
| frida-excel.mdc | **COMPLIANT** | Proper lifecycle, checkpointing, and resume logic |
| frida-sap.mdc | **PARTIAL** | Missing retry loops, input validation, and continue-on-error |
| frida-web.mdc | **N/A** | No web operations in this script |

---

## Detailed Compliance Findings

### frida-core.mdc - COMPLIANT

All core language rules are properly applied throughout the script.

| Rule | Status | Evidence |
|------|--------|----------|
| Single-line instructions | PASS | All instructions are single-line; no multi-line breaks |
| Block closings (`if`/`end`, `for`/`}`) | PASS | Correct throughout (lines 96-100, 106-112, 221-420, etc.) |
| Region organization | PASS | Uses `#%region`/`#%endregion` extensively (8+ regions) |
| Local variables use `<<<var>>>` | PASS | Consistent usage: `<<<Contador>>>`, `<<<home>>>`, `<<<runId>>>` |
| Global variables use `<<Var>>` | PASS | `<<sapUser>>`, `<<sapPass>>`, `<<excelFile>>` |
| String comparisons with quotes | PASS | `if ("<<<HeadersOk>>>" -ne "true")` (line 106) |
| List declaration before use | PASS | `DefineVariable type "List" as "ExpectedHeaders"` (line 38) |
| Operators (`-eq`, `-ne`, `-like`) | PASS | Used correctly: `-ne`, `-eq`, `-like` (line 227) |
| Comments syntax | PASS | Uses `##` for normal comments throughout |

**Example of correct boolean comparison (lines 96-100):**

```
if ("<<<actualHeader>>>" -ne "<<<expectedHeader>>>")
    DefineVariable as "HeadersOk" with the value "false"
    DefineVariable as "HeaderError" with the value "Header mismatch at col <<<col>>> | Expected: <<<expectedHeader>>> | Actual: <<<actualHeader>>>"
    break
end
```

---

### frida-excel.mdc - COMPLIANT

Excel operations follow all documented best practices.

| Rule | Status | Evidence |
|------|--------|----------|
| Workbook lifecycle (Load/Save/Close) | PASS | Load (lines 30-33), Save (404, 414), Close (432) |
| Checkpointing after each item | PASS | `Excel Save WBName` after each SUCCESS/FAIL |
| Header validation before processing | PASS | Lines 38-112 validate all 47 expected headers |
| Resume strategy with Processed sheet | PASS | Lines 116-138 implement deterministic resume |
| Always close workbooks | PASS | Line 432: `Excel Save WBName and close` |

**Resume logic implementation (lines 120-131):**

```
Excel ReadColumn from the worksheet {WSName} with the column index {1} start_at {2} and save its value as {TemplateColA} visible without nulls
CountItems in TemplateColA and save_as TotalTemplateRows

Excel ReadColumn from the worksheet {WSProcessed} with the column index {1} start_at {2} and save its value as {RowsProcessed} visible without nulls
CountItems in RowsProcessed and save_as TotalRowsProcessed

MathOperation <<<TotalRowsProcessed>>> + 2 and save as Contador
MathOperation <<<TotalTemplateRows>>> - <<<TotalRowsProcessed>>> and save as Remaining
```

**Checkpointing (lines 402-405):**

```
GetCurrentDate format={"MM/dd/yyyy HH:mm:ss" en} and save as NowHuman
Excel Append from WSProcessed at [1 ="<<<Contador>>>",2 ="SUCCESS",3 ="<<<NowHuman>>>",4 ="<<<runId>>>"]
Excel Save WBName
```

---

### frida-sap.mdc - PARTIALLY COMPLIANT

Several SAP-specific best practices are not fully implemented.

| Rule | Status | Evidence |
|------|--------|----------|
| Continue-on-error policy | MIXED | Uses `Finish` on row-level errors (line 418) |
| Evidence capture on failure | PASS | Line 410: `Titanium CaptureImage` |
| Systemic vs row-level error handling | NEEDS REVIEW | SAP login (line 144) has no try/catch |
| Validate data before SAP writes | MISSING | No validation of required fields |
| Guard against UI timing (retry loops) | MISSING | No retry logic for fragile SAP operations |

#### Issue 1: SAP Login Without Error Handling

**Current (line 144):**

```
SAP RunSapInstance "AMCO ECC - QE0 Quality" 060 <<sapUser>> <<sapPass>> EN graphic
```

**Recommended:**

```
try
    SAP RunSapInstance "AMCO ECC - QE0 Quality" 060 <<sapUser>> <<sapPass>> EN graphic
catch as ex
    Finish "SAP login failed - cannot continue: <<<ex>>>"
end
```

#### Issue 2: Finish on Row-Level Errors

**Current (lines 407-419):**

```
catch as ex
    Titanium CaptureImage and save as <<<evidenceDir>>>\SAP_Fail_Row<<<Contador>>>_<<<runId>>>.png
    GetCurrentDate format={"MM/dd/yyyy HH:mm:ss" en} and save as NowHuman
    Excel Append from WSProcessed at [1 ="<<<Contador>>>",2 ="FAIL",3 ="<<<NowHuman>>>",4 ="<<<runId>>>",5 ="<<<ex>>>"]
    Excel Save WBName
    Finish
end
```

Per frida-sap.mdc, row-level errors should log and continue rather than halt the entire batch. The script includes a comment acknowledging this is configurable, but the default behavior contradicts the rule.

#### Issue 3: Missing Input Validation

Required fields from Excel should be validated before SAP writes to prevent errors and wasted processing time.

**Recommended pattern:**

```
if ("<<<bp>>>" -eq "")
    Excel Append from WSProcessed at [1 ="<<<Contador>>>", 2 ="FAIL", 3 ="Missing BP"]
    Excel Save WBName
    Contador++
    continue
end
```

#### Issue 4: No Retry Loops for SAP UI Timing

SAP GUI can have timing issues. Fragile operations should use retry logic.

**Recommended pattern:**

```
DefineVariable type "int" as "attempts" with the value "0"
DefineVariable as "success" with the value "false"

while ("<<<success>>>" -ne "true") {
    try
        SAP WriteText ElementId wnd[0]/usr/ctxtP_ORG1 Text "<<<orgData>>>"
        DefineVariable as "success" with the value "true"
    catch as ex
        attempts++
        if (<<<attempts>>> > 3)
            ## Log and break out
            break
        end
        Sleep 1000
    end
}
```

---

### frida-web.mdc - NOT APPLICABLE

This script does not contain any web/browser operations. The frida-web.mdc rules are not applicable.

---

## New Patterns Identified

The following patterns in `Actions.txt` represent good practices that could be codified as formal rules.

### 1. Batch Processing Metadata Pattern

The script generates a unique run identifier for traceability:

```
GetCurrentDate format={"yyyy-MM-dd_HH-mm-ss" en} and save as RunStamp
DefineVariable as "runId" with the value "SAPBot_<<<RunStamp>>>"
```

This `runId` is included in all log entries and evidence filenames, enabling correlation across runs.

**Proposed Rule:** For batch scripts, generate a unique `runId` at startup using timestamp. Include this identifier in all log entries, evidence filenames, and notifications.

---

### 2. Structured Logging Schema Pattern

The script logs to a Processed sheet with consistent columns:

| Column | Content |
|--------|---------|
| 1 | Row number from Template |
| 2 | Status (SUCCESS/FAIL) |
| 3 | Timestamp |
| 4 | Run ID |
| 5 | Error message (on failure) |

**Proposed Rule:** Define a standard logging schema for batch operations:
- Column 1: Item identifier
- Column 2: Status code (SUCCESS/FAIL/SKIP)
- Column 3: Timestamp
- Column 4: Run ID
- Column 5: Error details (if applicable)

---

### 3. Decimal Normalization Pattern

The script handles SAP's locale-specific decimal format:

```
ReplaceFromVariable {marketPrice} this {.} for {,}
```

**Proposed Rule:** When writing numeric values to SAP, normalize decimal separators based on SAP locale settings. For European locales, replace `.` with `,`.

---

### 4. Transaction Reset Pattern

Each iteration starts with a fresh transaction to ensure consistent navigation state:

```
SAP StartTransaction zwb21
```

**Proposed Rule:** In batch SAP processing, start each iteration with `SAP StartTransaction` to reset navigation state and avoid accumulated UI state issues.

---

### 5. Evidence Directory Setup Pattern

The script ensures the evidence directory exists before attempting captures:

```
try
    File CheckIfDirExist in the path "<<<home>>>Documents" with the name "Frida_SAP_Evidence"
catch
    File NewFolder in "<<<home>>>Documents" with the name "Frida_SAP_Evidence"
end
```

**Proposed Rule:** Before capturing evidence, use try/catch to verify the target directory exists. Create it if missing to prevent capture failures.

---

### 6. Header Validation Loop Pattern

The script validates Excel headers before processing using a loop:

```
for 47 times {
    Excel ReadCellText from the worksheet {WSName} from the cell {1,<<<col>>>} and save its value as {actualHeader}
    DefineVariable as "expectedHeader" with the value "<<<ExpectedHeaders[<<<idx>>>]>>>"

    if ("<<<actualHeader>>>" -ne "<<<expectedHeader>>>")
        DefineVariable as "HeadersOk" with the value "false"
        break
    end
    col++
    idx++
}
```

**Proposed Rule:** For scripts dependent on specific Excel structures, validate all expected headers at startup and abort early with a clear error message if mismatched.

---

### 7. Characteristics Key-Value Mapping Pattern

The script uses a list of `"Key,Value"` pairs with regex extraction for dynamic mapping:

```
DefineVariable type "List" as "characteristics"
AddValueToList "characteristics" value "Certifications,<<<characteristicsCertifications>>>"

foreach item in characteristics {
    ApplyRegex ".+?(?=,)" to the string "<<<item>>>" and save as "charName"
    ApplyRegex "(?<=,).*$" to the string "<<<item>>>" and save as "charValue"
    ## Match and apply
}
```

**Proposed Rule:** For dynamic field mapping (e.g., SAP characteristics), use a list of `"Key,Value"` strings with regex extraction rather than hardcoding each field.

---

## Recommendations Summary

### High Priority

1. **Wrap SAP login in try/catch** - A login failure is systemic and should halt with a clear message. Do it
2. **Remove or configure `Finish` on row-level errors** - Default should be continue-on-error for batch processing. Do it
3. **Add input validation for required fields** - Validate `bp`, `material`, `plant`, etc. before SAP operations. Don't do it

### Medium Priority

4. **Add retry loops for fragile SAP operations** - Especially for UI writes and button clicks. Don't do it
5. **Document the new patterns** - Consider adding to frida-sap.mdc or creating a new frida-batch.mdc. Don't do it 

### Low Priority

6. **Parameterize the error handling policy** - Allow users to choose fail-fast vs continue-on-error via a global variable

---

## Conclusion

The script demonstrates strong adherence to FRIDA core language rules and Excel best practices. The primary gaps are in SAP-specific error handling patterns:

- **What's working well:** Region organization, variable syntax, Excel checkpointing, resume logic, evidence capture
- **What needs attention:** SAP login error handling, continue-on-error policy, input validation, retry loops

The script also showcases several patterns worthy of formal documentation as FRIDA rules, particularly around batch processing metadata, structured logging, and transaction reset strategies.
