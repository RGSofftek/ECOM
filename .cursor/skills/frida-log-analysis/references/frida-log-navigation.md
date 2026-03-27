---
name: frida-log-navigation
description: Generic, project-agnostic rules for reading and scanning FRIDA execution logs, defining log structure, error categories, scanning techniques, and how to add new patterns.
---

### Log structure and entry format

Most FRIDA execution log lines follow this structure:

- `<timestamp> - <Instruction> <details> : <Status>`
- `Status` is usually one of `Running`, `Success`, or `Error`.

Additional patterns:

- **Variable updates**:
  - `Se actualizo la variable :`
  - `Var Name : <name>`
  - `Value : <value>`
- **Comment echoes**:
  - `## <text> : Running / Success`
  - `#* <text> : Running / Success`
  - `#%region <name> : Running / Success`
  - `#%endregion : Running / Success`
- **.NET exceptions**:
  - `error: <Instruction> : <ExceptionType> (<code>): <message>`
  - Followed by stack trace lines.
  - Followed by a FRIDA line such as `<timestamp> - <Instruction> :  (Line: NNN) : Error`.
- **End-of-log footer**:
  - `SAPREADERENGINE LOG` block with initialization/termination metadata.

Treat comments and region markers as script-phase landmarks and exception blocks as anchors for failures.

### Error categories and investigation depth

For each error found, classify it before deciding how deep to investigate:

1. **Obvious error**
   - The log clearly states what went wrong and why.
   - Example: SAP status `\"E\"` with message `\"Incoterms 2 DAP is invalid\"`.
   - Action: explain in place, no further scanning required.

2. **Cascade (consequence) error**
   - An instruction failed as a consequence of an earlier failure in the same logical block.
   - Example: SAP rejects a value (E status), screen remains in error state, subsequent `ClickButton` fails with `COMException: The control could not be found by id`.
   - Action: trace the chain back to the originating failure and describe the relationship (cause -> effect).

3. **Ambiguous error**
   - The log alone does not fully explain the failure.
   - Example: `Excel Write ... : Error` with `Exception from HRESULT: 0x800401A8`.
   - Action: investigate further:
     - Check earlier log sections for related operations (e.g., earlier Excel actions).
     - Look for connection/initialization issues, or prior exceptions.
     - Cross-reference the FRIDA script (e.g. `Actions.txt`) to validate instruction syntax and parameters if available.

### Scanning techniques

- Start from the **end of the log** (tail-first).
- Search bottom-up for error markers:
  - `: Error`
  - `error:`
  - `Exception`
- For each error:
  - Scan upward for the **nearest comment or region marker** (`##`, `#*`, `#%region`, `#%endregion`) to determine which logical phase of the script was executing.
  - Identify the **instruction and parameters** involved (e.g. SAP element id, text value, Excel target cell/range).
  - Decide if the error is **obvious**, **cascade**, or **ambiguous**.
- For ambiguous errors:
  - Expand the search window to earlier lines of the same type of operation.
  - Check variable updates immediately preceding the failure for unexpected values.
  - Look for loops that exhausted all items without a match (e.g. many `If Result : False` with no `break`).
- Always report all errors found, clearly distinguishing **root causes** from **downstream consequences**.

### Variable lifecycle tracing

When an error is caused by the **input of a variable** (value sent to SAP, written to Excel, or used in a condition), trace that variable’s **definition and lifecycle** in the log to see where the value went wrong:

- **Definition**: Where the variable was set (e.g. `Excel ReadCell` / `ReadCellText` → "Var Name" / "Value", or `DefineVariable` → "Value").
- **Transforms**: Any changes along the way (e.g. `ReplaceFromVariable`, `ApplyRegex`, list indexing).
- **Consumption**: Where the value was used (e.g. `WriteText` with `Text "..."`, `Excel Write`, or the failing instruction).

Check each step to decide whether the problem is at definition (bad source data), in a transform (wrong logic), or at consumption (e.g. wrong target or a system reporting quirk). This works even without the script: search the log for the variable name in "Var Name" / "Value" and in the failing instruction’s parameters.

**SAP field value vs. reported value**

When an SAP error message mentions a field value (code, month, amount):

1. Find the most recent `WriteText` to the same element ID in the log and extract the `Text "..."` value (consumption).
2. Compare that written value with what SAP reports in the error. If they differ, flag a **SAP-reporting discrepancy** (e.g. SAP reports default instead of the value actually sent).
3. Trace back to the variable’s definition (e.g. "Value :" after Excel read or DefineVariable) to confirm the source value and complete the lifecycle.

### Adding new patterns

When you discover a new **structural** pattern in logs (not just a single project-specific bug), add it here to improve future navigation:

1. Capture a minimal excerpt (2–5 lines) that uniquely illustrates the pattern.
2. Describe:
   - What makes this pattern distinct.
   - How to detect it (keywords, shapes, repetition).
   - How it should influence scanning or classification.
3. Keep examples short to avoid bloating this file.

**RunScript (sub-scripts)**  
Scripts can call sub-scripts via `RunScript <name>.txt`. In the log this appears as an entry `RunScript <name> : Running` (then `Success` or `Error`), and the sub-script’s instructions are emitted **inline** in the same log. When tracing a failure, if the failing instruction is not found in the main script near the reported line number, look for a **preceding** `RunScript <name>` log entry; the failing line may belong to that sub-script. Open the corresponding sub-script file (e.g. `<name>.txt`) to understand and fix the logic.

Project-specific, user-confirmed diagnoses should be added to `frida-log-learnings.md`, not here.

