# CLAUDE.md

> **Priority: P0 — Claude Code Entry Point**

This repository uses `AGENTS.md` as the primary agent instruction and orchestration file.

## Required Behavior

Before performing any substantial task in this repository:

1. Read `AGENTS.md` from the repository root.
2. Follow all applicable instructions defined there.
3. Discover and use relevant skills according to the Skill-First Policy in `AGENTS.md`.
4. Read the selected skill's `SKILL.md` before using that skill.
5. Use the smallest sufficient set of skills for the task.
6. Respect repository structure, code priority labels, notebook rules, research methodology, reproducibility requirements, and Thai technical explanation rules defined in `AGENTS.md`.

## Source of Truth

Instruction priority for this repository:

```text
User Request
    ↓
CLAUDE.md
    ↓
AGENTS.md
    ↓
Task-Specific / Specialized SKILL.md
    ↓
General SKILL.md
    ↓
Default Claude Behavior
```

`CLAUDE.md` intentionally contains minimal duplicated guidance.

For detailed repository rules, workflows, research practices, notebook conventions, skill orchestration, and validation requirements, always refer to:

```text
./AGENTS.md
```

## Skills

Expected skill location:

```text
.agents/skills/
```

When a relevant skill exists:

```text
Task
  ↓
Read AGENTS.md
  ↓
Discover relevant skill
  ↓
Read SKILL.md
  ↓
Execute
  ↓
Validate
```

Do not recreate an existing skill workflow manually unless the skill is unavailable or clearly unsuitable.

## Language

Follow the language policy defined in `AGENTS.md`.

For AI/ML research and notebook explanations, Thai should normally be the primary explanatory language while preserving standard English technical terminology.

## Final Rule

Do not treat `CLAUDE.md` as a replacement for `AGENTS.md`.

Treat it as the Claude-specific bootstrap file that directs Claude to the repository-wide agent contract.
