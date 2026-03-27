# Plan Review (review plan → present findings → clarify ambiguous → apply corrections)

Review the current plan for redundancies, inconsistencies, errors, and poorly written code syntax. Use the **plan-reviewer** subagent so the planning context window stays lean. Present all findings, ask once for clarification on ambiguous items, then apply approved corrections directly to the plan file.

## Target plan (in order)

1. If the user typed a path after the command (e.g. `plan-review cover_month_early_validation.plan.md`), use that `.plan.md` file. Resolve it relative to `.cursor/plans/` or the workspace root as appropriate.
2. If a plan is actively referenced or visible in the current conversation context (e.g. a `.plan.md` was attached, linked, or mentioned by path), use that plan.
3. Otherwise, pick the **most recently modified** `.plan.md` in `.cursor/plans/` (workspace path).
4. If no plan exists, report "No plan found" and stop.

## Workflow

### Step 1 – Resolve plan and extract references

1. Read the resolved plan file.
2. Extract all file paths referenced in the plan (markdown links, code blocks, "in Actions.txt", "lines 420–430", etc.). Resolve each path relative to the workspace root; keep only paths that exist on disk in **referencedFiles**.

### Step 2 – Run the plan-reviewer subagent

1. Launch the **plan-reviewer** subagent via **mcp_task** with:
   - **planPath**: absolute path to the plan file.
   - **referencedFiles**: the list of extracted file paths that exist.
2. In the task prompt, instruct the subagent to review the plan at `planPath` and cross-check against `referencedFiles`, then return the structured Plan Review Report (Errors, Warnings, Info, Ambiguous).
3. Capture the subagent’s full response (the report text).

### Step 3 – Present findings

1. Parse the report into four lists: **Errors**, **Warnings**, **Info**, **Ambiguous**.
2. In chat, present all findings grouped by severity (Errors first, then Warnings, then Info). For each item, include enough detail (step number, line range, or snippet) so the user can approve or dismiss it.
3. If there are **Ambiguous** items, collect them and call **AskQuestion** once (batch): present the ambiguous questions and offer options such as "Answer in chat", "Ignore these", "Apply suggested fix for [item]", etc., so the user can clarify in one go.

### Step 4 – Apply corrections after user responds

1. For each **resolved ambiguity** and each **approved Error or Warning fix**: apply the correction directly to the plan file using **StrReplace** on the plan path. Make only the edits that correspond to user-approved items.
2. For items the user **dismisses** or marks as "ignore": do not change the plan; note them in the final summary.
3. Report a **final summary** in chat:
   - What was corrected (and where in the plan).
   - What was dismissed.
   - Any remaining Info items (no change applied unless the user asked to fix them).

## Summary

- The **plan-reviewer** subagent is readonly; all edits to the plan file are done by the main agent after user approval.
- Prefer **one AskQuestion** for all ambiguous items to avoid back-and-forth.
- Do not edit the plan file until the user has approved (all or a subset) of the proposed corrections.
