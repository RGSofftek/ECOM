---
name: frida-log-analysis
description: Analyze FRIDA execution logs (.txt) from C:\FRIDA\TuringExpo\Local\3129455\Logs. Fetches the latest log via a PowerShell helper, classifies errors as obvious, cascade, or ambiguous, consults navigation and learnings references, and delegates deep dives to the frida-log-debugger subagent. Use when inspecting a FRIDA run, debugging failures, or understanding what happened during automation.
---

### Purpose

This skill helps the agent reliably fetch and analyze the latest FRIDA execution log from `C:\FRIDA\TuringExpo\Local\3129455\Logs`, using:

- A PowerShell helper (`scripts/get_latest_frida_log.ps1`) to find the latest `.txt` log and optionally return a tail of lines.
- Generic navigation rules (`references/frida-log-navigation.md`) for understanding FRIDA log structure, classifying errors, and scanning effectively.
- A learnings file (`references/frida-log-learnings.md`) to reuse user-confirmed diagnoses from past debugging sessions.
- A dedicated subagent (`frida-log-debugger`) for deep, isolated log analysis when needed.

### When to use this skill

Use this skill whenever:

- The user asks to \"check the last FRIDA log\" or \"see what happened\" in a FRIDA run.
- The user reports a failure or unexpected behavior in a FRIDA process and wants to understand why.
- You need to analyze FRIDA logs stored in `C:\FRIDA\TuringExpo\Local\3129455\Logs`.

### Tiered workflow

1. **Fetch the latest log tail**
   - Run `scripts/get_latest_frida_log.ps1` via the shell tool, typically with a tail:
     - Example: `get_latest_frida_log.ps1 -Tail 600 -IncludeContent`.
   - Extract the `path` and `tailLines` from the JSON output when `-IncludeContent` is used.

2. **Quick scan and classification**
   - Using the tail, apply the rules from `references/frida-log-navigation.md`:
     - Identify error lines (markers like `: Error`, `error:`, `Exception`).
     - For each error, classify it as:
       - **Obvious** (log clearly states cause).
       - **Cascade** (downstream consequence of an earlier failure).
       - **Ambiguous** (log alone does not fully explain cause).
   - Look at nearby comments and regions (`##`, `#%region`, `#%endregion`) to understand where in the script the error occurred.

3. **Check for known patterns**
   - Before forming conclusions, consult `references/frida-log-learnings.md`:
     - If a known pattern matches the error excerpt, reuse the confirmed root cause and resolution.

4. **Decide investigation depth**
   - If all errors are **obvious** or **clearly cascading**, and the tail gives enough context:
     - Explain findings directly in the main context.
   - If any error is **ambiguous**, if the log is large/complex, or if the user asks for a thorough analysis:
     - Invoke the `frida-log-debugger` subagent with:
       - The full log path.
       - The list of known error lines (or snippets).
       - Optionally, the FRIDA script path (e.g. `Actions.txt`) for cross-referencing.

5. **Present findings and capture learnings**
   - Summarize:
     - Root cause errors and any cascade relationships.
     - Ambiguous areas and what was investigated.
     - Suggested next steps (data to fix, script sections to review, environment issues to check).
   - After the user verifies and reports back with actual findings:
     - Add a new entry to `references/frida-log-learnings.md` for any newly confirmed pattern.

### Example end-to-end Cursor workflow

You can follow this workflow when asking Cursor to debug a FRIDA run:

1. In a chat, say: "Use the `frida-log-analysis` skill to check the last FRIDA log; the process failed during contract creation."
2. The agent uses `frida-log-analysis` to:
   - Run `get_latest_frida_log.ps1` and retrieve the latest log tail and path.
   - Apply `frida-log-navigation.md` to classify errors and understand context.
   - Consult `frida-log-learnings.md` to reuse any known patterns.
3. If the agent finds only obvious or clearly cascading errors, it explains them directly; otherwise it invokes the `frida-log-debugger` subagent for a deep dive.
4. The subagent reads targeted slices of the log (and `Actions.txt` if needed), then returns a structured report with root causes, cascades, ambiguous areas, and recommendations.
5. You verify the report against SAP/Excel/data, then tell the agent what you found; the agent adds new confirmed patterns to `frida-log-learnings.md` so similar issues are recognized faster in the future.

### Files this skill relies on

- `scripts/get_latest_frida_log.ps1`:
  - Finds the latest `.txt` log in `C:\FRIDA\TuringExpo\Local\3129455\Logs`.
  - Supports:
    - `-Tail <int>` to return the last N lines.
    - `-IncludeContent` to emit JSON `{ path, lastWriteTime, tailLines }`.

- `references/frida-log-navigation.md`:
  - Describes FRIDA log structure and common line formats.
  - Defines error categories (obvious, cascade, ambiguous).
  - Provides scanning techniques and an \"adding new patterns\" section for structural patterns.

- `references/frida-log-learnings.md`:
  - Stores project-specific, user-confirmed diagnoses and resolutions.
  - Should be consulted after error detection and before final conclusions.

- `.cursor/agents/frida-log-debugger.md`:
  - Subagent used for deep-dive, isolated log analysis (large logs, ambiguous errors, cross-referencing with scripts).

