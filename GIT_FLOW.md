# Git Workflow

> Priority: P1 — Repository Git Rules

This repository uses a lightweight trunk-based workflow.

The primary branch is:

```text
main
```

`main` should remain usable and reproducible.

---

# Branch Model

```text
main
 │
 ├── feat/*
 ├── fix/*
 ├── docs/*
 ├── experiment/*
 ├── refactor/*
 └── chore/*
```

Do not maintain a permanent `develop` branch unless project scale requires it.

---

# Branch Naming

## Feature

```text
feat/<short-name>
```

Example:

```text
feat/bert-pretraining-lab
```

## Experiment

```text
experiment/<short-name>
```

Example:

```text
experiment/gqa-memory-benchmark
```

## Fix

```text
fix/<short-name>
```

Example:

```text
fix/attention-mask-shape
```

## Documentation

```text
docs/<short-name>
```

## Refactoring

```text
refactor/<short-name>
```

## Maintenance

```text
chore/<short-name>
```

---

# Starting Work

Always update local `main` first.

```bash
git switch main
git pull --rebase
```

Create branch:

```bash
git switch -c feat/rope-lab
```

---

# Before Commit

Check:

```bash
git status
git diff
```

Run relevant validation.

```bash
uv run ruff check .
uv run pytest
```

Notebook changes should also be executed from a clean kernel.

---

# Commit Style

Use small logical commits.

Prefer:

```text
feat(rope): add rotary embedding implementation
test(rope): add position rotation checks
docs(rope): explain frequency construction
```

Avoid:

```text
update
fix stuff
changes
final
final2
```

---

# Amend

If the latest commit has not been shared:

```bash
git add .
git commit --amend --no-edit
```

Change message:

```bash
git commit --amend
```

Avoid rewriting commits already used by other collaborators unless coordinated.

---

# Stash

Use stash when switching context without committing incomplete work.

```bash
git stash push -m "wip: rope experiment"
```

List:

```bash
git stash list
```

Restore and keep stash:

```bash
git stash apply
```

Restore and remove stash:

```bash
git stash pop
```

Use `apply` when uncertain.

Use `pop` when confident the stash can be removed.

---

# Rebase

Before opening a PR:

```bash
git fetch origin
git rebase origin/main
```

If conflicts occur:

```bash
git status
```

Resolve files, then:

```bash
git add <resolved-file>
git rebase --continue
```

Abort if needed:

```bash
git rebase --abort
```

---

# Rebase Rule

Prefer:

```text
rebase local feature branch onto main
```

Avoid rebasing:

```text
shared public branches
```

without coordination.

---

# Merge Strategy

Preferred PR strategy:

```text
Squash Merge
```

for small feature/experiment branches.

Use regular merge when commit history itself contains meaningful research stages.

Example:

```text
baseline
→ optimized implementation
→ benchmark
→ analysis
```

may deserve preserved commits.

---

# Experimental Branches

Experiments may be short-lived.

Example:

```text
experiment/muon-vs-adamw
```

If successful:

```text
experiment
   ↓
validate
   ↓
refactor
   ↓
merge into main
```

If unsuccessful:

Document useful findings and delete the branch.

Failed experiments can still produce valuable knowledge.

---

# Conflict Resolution Rule

Never blindly choose:

```text
Accept Current
Accept Incoming
```

For code or notebook conflicts.

Understand what each side changed.

For `.ipynb` conflicts, prefer recreating or re-running the notebook when merge state becomes unreliable.

---

# Force Push

Allowed only on your own feature branches after rebase:

```bash
git push --force-with-lease
```

Prefer:

```text
--force-with-lease
```

Never use plain:

```text
--force
```

unless there is a specific justified reason.

---

# Cleanup

After PR merge:

```bash
git switch main
git pull --rebase
git branch -d feat/rope-lab
```

Prune remote references:

```bash
git fetch --prune
```

---

# Recommended Daily Workflow

```text
git switch main
      ↓
git pull --rebase
      ↓
git switch -c <branch>
      ↓
work
      ↓
git diff
      ↓
test
      ↓
commit
      ↓
git fetch origin
      ↓
git rebase origin/main
      ↓
push
      ↓
PR
      ↓
review
      ↓
merge
      ↓
delete branch
```

---

# Core Principle

Git history should explain the evolution of the work.

It should not become a storage location for random intermediate states.
