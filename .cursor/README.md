# frida-dev-tools

Shared FRIDA development assets for Cursor-based projects: agents, commands, rules, skills, reader documentation, and helper scripts.

This repository is the **canonical contents of project root `.cursor/`**. Consume it with `git subtree` so each project keeps `.cursor/rules`, `.cursor/commands`, and `.cursor/skills` where Cursor expects them.

## Layout

| Path | Purpose |
|------|---------|
| `agents/` | Cursor agent definitions |
| `commands/` | Cursor slash commands (e.g. frida-lint-fix, plan-review) |
| `rules/` | Cursor rules (`.mdc`) for FRIDA workflows |
| `skills/` | Cursor skills (e.g. frida-log-analysis) |
| `docs/` | FRIDA reader reference markdown |
| `tools/` | Shared scripts (e.g. `frida_lint.py`) |

Do **not** put project-specific automation here (e.g. one-off template fixers). Keep those in the consumer repo outside this subtree.

## Install in a consumer repo

Use a dedicated remote (example name `frida-tooling`) so `origin` stays the project’s main remote.

```bash
git remote add frida-tooling https://github.com/RGSofftek/frida-dev-tools.git
git fetch frida-tooling
git subtree add --prefix=.cursor frida-tooling main --squash
```

If `.cursor` already exists and is tracked, remove it first (one commit), then run `subtree add` so the prefix is not occupied.

## Pull updates

```bash
git fetch frida-tooling
git subtree pull --prefix=.cursor frida-tooling main --squash
```

## Push changes upstream

Commit changes under `.cursor` in the consumer repo, then:

```bash
git subtree push --prefix=.cursor frida-tooling main
```

## Tooling paths

- Reader docs: `.cursor/docs/...`
- Linter (from **project root**): `python .cursor/tools/frida_lint.py format|check ...`

Project root keeps `.fridalintrc` and other project-local files as today.
