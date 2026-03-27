# Agent tools and how to instruct the prompt

This document lists the tools available to the Cursor agent and when Cursor instructs the agent to use them. It also describes how **you** can instruct the prompt (via mode, commands, or rules) so the agent uses specific tools or behaviors.

---

## 1. Tools available to the agent

| Tool | Purpose |
|------|--------|
| **Read** | Read file contents or image files. |
| **Write** | Create or overwrite a file. |
| **StrReplace** | Exact string replacement in a file. |
| **Grep** | Search codebase/content (ripgrep-style). |
| **Glob** | Find files by glob pattern (e.g. `**/*.ts`). |
| **Delete** | Delete a file. |
| **Shell** | Run a command in the terminal. |
| **ReadLints** | Read linter/diagnostic errors for files or folders. |
| **EditNotebook** | Edit Jupyter notebook cells. |
| **TodoWrite** | Create or update a todo list (merge/replace). |
| **AskQuestion** | Present structured multiple-choice questions to the user. |
| **CreatePlan** | Create a plan in markdown (with optional todos). |
| **WebSearch** | Search the web. |
| **mcp_web_fetch** | Fetch content from a URL. |
| **GenerateImage** | Generate an image from a text description. |
| **mcp_task** | Launch a subagent (e.g. explore, shell, frida-log-debugger). |

---

## 2. When Cursor tells the agent to use each tool

- **AskQuestion** – In Plan mode: “Use the AskQuestion tool to present [clarifying questions] to the user.” In general instructions: when the agent needs to ask something, use AskQuestion for structured options.
- **CreatePlan** – In Plan mode: “Present your plan by calling the CreatePlan tool” and “Do not make any file changes … until the user has confirmed the plan.”
- **TodoWrite** – Use for complex multi-step tasks, when the user asks for a todo list, or when the user gives multiple tasks. Skip for simple or single-step tasks.
- **Shell** – Prefer specialized tools (Read, Write, Grep) over terminal when possible; use Shell for commands that must run in the terminal.
- **Read** – Use for file contents; do not use terminal commands to read files.
- **Grep** – Prefer Grep over running `grep`/`find` in the terminal.
- **GenerateImage** – Only when the user explicitly asks for an image; not for charts/tables (use code).
- **mcp_task** – For complex or broad exploration; use narrower tools (Grep, Read) for specific lookups.

Other tools (Write, StrReplace, Delete, Glob, EditNotebook, WebSearch, mcp_web_fetch) are used when they fit the task; Cursor does not give special “when to use” rules for them.

---

## 3. How to instruct the prompt so the agent uses these tools

### 3.1 AskQuestion and CreatePlan (plan-first behavior)

**Option A – Use Cursor Plan mode**

- Turn **Plan mode** on for the conversation (Cursor UI).
- Cursor then instructs the agent to use **AskQuestion** for clarifying questions and **CreatePlan** to present the plan, and not to make edits until you confirm.
- No project files required.

**Option B – Project rule or command (same behavior without requiring Plan mode)**

- In a **rule** (e.g. `.cursor/rules/plan-first-workflow.mdc`): state that for “plan-first” workflows the agent must (1) ask 1–2 clarifying questions (in chat or via AskQuestion if available), (2) draft a plan in markdown (or use CreatePlan if available), (3) wait for explicit approval before making edits.
- In a **command** (e.g. `.cursor/commands/plan-first.md`): add “This is a plan-first workflow. Apply the plan-first rule: clarify → plan → wait for approval → execute.”
- When you run that command or when the rule applies, the agent will follow that flow; in Plan mode it can use the actual AskQuestion and CreatePlan tools.

**Example prompt you can type**

- “Use plan mode for this” (and enable Plan mode), or  
- “Run the plan-first command for: [your task]”, or  
- “This is a plan-first task: [your task]. Ask clarifying questions, then propose a plan and wait for my approval before changing anything.”

---

### 3.2 TodoWrite (task list)

**How to get the agent to use TodoWrite**

- Ask for a task list or breakdown: “Give me a todo list for …”, “Break this down into steps and track them.”
- Or describe a multi-step task: “Implement X, Y, and Z” or “Refactor this in stages.”
- The agent is instructed to use TodoWrite for complex/multi-step tasks, so being explicit about steps or asking for a list encourages it.

**Example prompts**

- “Create a todo list for migrating the FRIDA script to the new reader.”
- “Break this into steps and track progress with todos.”

---

### 3.3 Shell (terminal)

**How to get the agent to use Shell**

- Ask to run a specific command: “Run `python .cursor/tools/frida_lint.py check Actions.txt`.”
- Ask for setup or install: “Install dependencies”, “Run the tests.”
- The agent is instructed to prefer Read/Grep/Write over terminal for file operations; for actual commands (tests, linters, scripts), asking explicitly for “run …” or “execute …” leads to Shell.

**Example prompts**

- “Run the linter on Actions.txt.”
- “Execute the tests and show the output.”

---

### 3.4 GenerateImage

**How to get the agent to use GenerateImage**

- Ask explicitly for an image: “Generate an image of …”, “Create an icon for …”, “Make a mockup of ….”
- The agent is instructed to use GenerateImage only when you explicitly ask for an image; do not use it for data charts or tables (those are done with code).

**Example prompts**

- “Generate an app icon for a note-taking app, minimal flat style.”
- “Create a UI mockup of the settings screen.”

---

### 3.5 mcp_task (subagents)

**How to get the agent to use mcp_task**

- Ask for broad exploration or multi-step investigation: “Explore the codebase for …”, “Find all places that …”, “Run this in a subagent.”
- The agent is instructed to use mcp_task for complex or broad tasks and to use Grep/Read for narrow lookups.

**Example prompts**

- “Explore how API endpoints are defined in this project.”
- “Have a subagent analyze the FRIDA log and return a structured report.”

---

### 3.6 Read, Grep, Glob, Write, StrReplace, Delete, ReadLints, EditNotebook

**How to get the agent to use these**

- Describe the task normally; the agent chooses the tool.
- Being specific helps: “Search for `SAP WriteText` in the repo” → Grep; “Show me the contents of Actions.txt” → Read; “Add a new rule to frida-core.mdc” → Read + StrReplace/Write; “Fix the linter errors in this file” → ReadLints then edits.

**Example prompts**

- “Find all uses of RunScript in the FRIDA scripts.”
- “Read the first 50 lines of Actions.txt and suggest a checkpoint comment.”
- “Fix the lint errors reported in .cursor/tools/frida_lint.py.”

---

## 4. Summary: instructing the prompt by goal

| Goal | What to do or say |
|------|-------------------|
| Clarifying questions + plan before edits | Enable Plan mode, or use a plan-first command/rule and say “plan-first” or “ask then plan, wait for approval.” |
| Task list / progress tracking | Ask for a “todo list” or describe a “multi-step” or “complex” task. |
| Run a command or script | Ask to “run …”, “execute …”, “install …”, or “run the linter/tests.” |
| Generate an image | Explicitly ask to “generate an image” or “create a mockup/icon.” |
| Broad exploration / subagent | Ask to “explore the codebase” or “have a subagent analyze ….” |
| Search, read, edit, lint | Describe the task; be specific (e.g. “search for X”, “read file Y”, “fix lint in Z”). |

---

*Defines agent tools and how to instruct the prompt so you can reliably trigger the behavior you want.*
