# Contributing

> Priority: P1 — Repository Contribution Standard

This repository is an AI Research & Engineering Lab.

Contributions should improve understanding, reproducibility, implementation quality, or engineering insight.

---

## Before Contributing

Read:

1. `AGENTS.md`
2. `README.md`
3. `GIT_FLOW.md`
4. relevant `labs/<topic>/README.md`
5. applicable `.agents/skills/*/SKILL.md`

---

## Contribution Types

Accepted contributions include:

* new research paper labs
* notebook improvements
* mathematical explanations
* PyTorch implementations
* experiment design
* benchmark results
* reproducibility improvements
* engineering notes
* bug fixes
* documentation improvements

---

## Branch Naming

Use:

```text
feat/<topic>
fix/<topic>
docs/<topic>
refactor/<topic>
experiment/<topic>
chore/<topic>
```

Examples:

```text
feat/rope-lab
experiment/flashattention-memory
docs/chinchilla-notes
fix/gpt2-tokenizer
refactor/shared-attention
```

---

## Code Priority

All meaningful implementation changes should follow:

```text
P0 — Core / Critical
P1 — Important / Reusable
P2 — Convenience / Analysis
P3 — Experimental / Disposable
```

Experimental code should be clearly identifiable and easy to remove.

---

## Notebook Rules

Notebooks must:

* run top-to-bottom
* avoid hidden state
* explain objectives
* define prerequisites
* state hypotheses where applicable
* show tensor shapes
* explain important equations
* include observations
* separate findings from interpretation
* document limitations

Before submission:

```text
Restart Kernel
→ Run All
→ Verify output
```

---

## Shared Code

Reusable code should not remain duplicated across notebooks.

When an implementation is used by multiple labs, consider moving it into:

```text
shared/src/
```

---

## Dependency Changes

Use:

```bash
uv add <package>
```

or:

```bash
uv add --dev <package>
```

Do not manually modify dependency versions without updating:

```text
pyproject.toml
uv.lock
```

Avoid introducing additional dependency managers.

---

## Commit Convention

Use Conventional Commits.

Examples:

```text
feat: add RoPE implementation lab
fix: correct attention mask broadcasting
docs: add Chinchilla engineering notes
refactor: extract shared attention utilities
test: add scaled attention tests
experiment: compare MQA and GQA memory usage
chore: update uv lockfile
```

Recommended format:

```text
<type>(optional-scope): <description>
```

Types:

```text
feat
fix
docs
refactor
test
experiment
perf
chore
ci
build
```

---

## Pull Request Requirements

A pull request should explain:

* what changed
* why it changed
* affected lab/topic
* experiment impact
* dependency changes
* validation performed
* known limitations

Avoid mixing unrelated changes in one PR.

---

## Validation

Before opening a PR:

```bash
uv sync --locked
uv run ruff check .
uv run pytest
docker compose config
```

For notebook changes, also verify:

```text
Restart Kernel
→ Run All
```

---

## Research Integrity

Clearly distinguish:

* Paper Finding
* Author Claim
* Experimental Evidence
* Interpretation
* Engineering Implication
* Hypothesis

Do not present personal interpretation as a result reported by the paper.

---

## Definition of Done

A contribution is ready when:

```text
[ ] scope is clear
[ ] relevant skills were followed
[ ] notebook executes correctly
[ ] code is understandable
[ ] experiment is reproducible
[ ] findings and interpretation are separated
[ ] limitations are documented
[ ] lint/tests pass
[ ] CHANGELOG updated when appropriate
```
