---
name: frida-log-learnings
description: Persistent memory of user-confirmed FRIDA log diagnoses and resolutions, to be consulted after error detection and before presenting conclusions.
---

# FRIDA Log Learnings

Consult this file after finding errors and before presenting conclusions.
If a known pattern matches, use the confirmed root cause and resolution instead of guessing.

## Known error patterns

### SAP ClickButton: control not found by id
- **First seen**: 2026-03-03
- **Log excerpt**:
  ```text
  3/3/2026 12:27:33 PM - SAP ClickButton id wnd[0]/tbar[1]/btn[7] : Running
  3/3/2026 12:27:33 PM - error: ClickButton id wnd[0]/tbar[1]/btn[7] : System.Runtime.InteropServices.COMException (0x0000026B): The control could not be found by id.
  3/3/2026 12:27:33 PM - SAP ClickButton id wnd[0]/tbar[1]/btn[7] :  (Line: 397) : Error
  3/3/2026 12:27:36 PM - ## Continue-on-error: log failure and proceed to next row : Success
  ```
- **Actual root cause**: SAP screen was in an unexpected state (e.g., error dialog or different layout), so the toolbar button with id `wnd[0]/tbar[1]/btn[7]` was not present when FRIDA tried to click it.
- **Resolution**: Ensure that the script only attempts this click when the expected screen is active, or add guard checks (e.g., verify status messages, check screen elements) before clicking. Treat this as a cascade error when an upstream SAP validation error is present.

### SAP WriteText: COMException invalid argument
- **First seen**: 2026-03-03
- **Log excerpt**:
  ```text
  3/2/2026 4:49:40 PM - SAP WriteText ElementId wnd[0]/usr/subSS_HD_PRICE_DETAILS:ZACMRE_DEAL_CONTRACT:2800/ctxtSG_HEADER_PRICE_SC-COVER_MONTH_VAL Text "" : Running
  3/2/2026 4:49:40 PM - error: WriteText ElementId wnd[0]/usr/subSS_HD_PRICE_DETAILS:ZACMRE_DEAL_CONTRACT:2800/ctxtSG_HEADER_PRICE_SC-COVER_MONTH_VAL Text "" : System.Runtime.InteropServices.COMException (0x00000265): The method got an invalid argument.
  3/2/2026 4:49:40 PM - SAP WriteText ElementId wnd[0]/usr/subSS_HD_PRICE_DETAILS:ZACMRE_DEAL_CONTRACT:2800/ctxtSG_HEADER_PRICE_SC-COVER_MONTH_VAL Text "" :  (Line: 455) : Error
  ```
- **Actual root cause**: FRIDA attempted to write an empty or invalid value into a SAP text field that does not accept that argument (e.g., required field or constrained domain).
- **Resolution**: Validate the value before writing (ensure it is non-empty and within expected domain), or adjust the script so it skips/handles cases where the value is not valid for the target field.

### Excel LoadWBook: document missing or corrupted
- **First seen**: 2026-03-03
- **Log excerpt**:
  ```text
  3/3/2026 12:19:43 PM - Excel LoadWBook "<<excelFile>>" as WBName : Running
  3/3/2026 12:19:45 PM - Error loading the book, please verify that the document exists or is not corrupted.
  3/3/2026 12:19:45 PM - Excel LoadWBook "<<excelFile>>" as WBName : (Line: 40) : Error
  ```
- **Actual root cause**: Excel workbook could not be opened (file path wrong, file missing, file locked, or corrupted).
- **Resolution**: Verify the `excelFile` path, ensure the file exists and is accessible, and check that no other process is locking or corrupting the workbook before running the FRIDA process.

### WriteText BID-BASE_PRICE_VAL: invalid argument (cascade after Cover Month invalid)
- **First seen**: 2026-03-04
- **Log excerpt**:
  ```text
  lastSAPError with the value "SAP(E) [ZACM000]: Cover Month KCK6 is invalid"
  ...
  SAP WriteText ElementId .../txt<SG>-BID-BASE_PRICE_VAL Text "1000" : Running
  error: WriteText ... : COMException (0x00000265): The method got an invalid argument.
  SAP WriteText ... : (Line: 433) : Error
  ```
- **Actual root cause**: SAP had already rejected Cover Month. **SAP reporting discrepancy**: SAP often reports the **default** value (e.g. KCK6) in the error message, not the value that was actually written from Excel (e.g. KCH6). The **actual invalid value** is the one from Excel/source; use variable lifecycle tracing (last WriteText to COVER_MONTH_VAL, then "Value :" from Excel read) to confirm. The BID WriteText failure is a **cascade** — the script continued to Price Detail (BID) and tried to write to BID-BASE_PRICE_VAL while the screen had that validation error, so WriteText threw invalid argument.
- **Resolution**: Fix the Cover Month value in Excel/source data so SAP accepts it (valid domain/format for the contract type). The script now validates Cover Month **before** the Characteristics loop (region "Price Detail (Cover Month)" after Basic Data). If CheckSAPStatus sets lastSAPError (e.g. Cover Month invalid), the script enriches the message with the Excel value and skips Characteristics, Price Detail, Texts, Rules, and Finalize — so the log shows the enriched Cover Month error and no BID cascade.

### Stale "Fill required fields" when GetStatusInfo throws (control not found)
- **First seen**: 2026-03-03
- **Log excerpt**:
  ```text
  SAP ClickButton id wnd[0]/tbar[1]/btn[8] : Success
  SAP GetStatusInfo as StatInfo : Running
  error: GetStatusInfo as StatInfo : System.Runtime.InteropServices.COMException (0x0000026B): The control could not be found by id.
  SAP GetStatusInfo as StatInfo :  (Line: 509) : Error
  ...
  If Evaluation Expression : ("SAP(E) [ZACM000]: Fill required fields" -ne "")
  If Result : True
  DefineVariable as "errorDetail" with the value "Price Details (BID): SAP(E) [ZACM000]: Fill required fields"
  ```
- **Actual root cause**: The **failing** instruction is `GetStatusInfo` (after clicking btn[8]): the status bar control could not be found (screen may have changed, e.g. dialog or different layout). The message "Fill required fields" is **stale** — it was set by an **earlier** successful GetStatusInfo in the same row (after BID WriteText + SendKey 0). The catch block uses `lastSAPError` when non-empty, so it reports that old message instead of the real failure (control not found). The Excel field is not missing; the script is misreporting.
- **Resolution**: In the script, clear `lastSAPError` before the GetStatusInfo that runs after a button click (e.g. before line 509), and in the catch when both `lastSAPError` and `ex` are empty, set errorDetail to a message like "SAP status could not be read (screen may have changed)". So the reported error reflects the actual failure instead of a previous SAP message.

<!--
Template for new entries:

### [Pattern title]
- **First seen**: [YYYY-MM-DD]
- **Log excerpt**:
  ```text
  [2–5 key lines showing the pattern]
  ```
- **Actual root cause**: [user-confirmed explanation]
- **Resolution**: [how it was fixed or what to check]
-->

