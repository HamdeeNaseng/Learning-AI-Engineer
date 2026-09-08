# Pull Request

## Summary

<!-- What changed? Keep this concise. -->

## Why

<!-- Why is this change needed? What problem, research question, or engineering issue does it address? -->

## Change Type

* [ ] `feat` — new lab or functionality
* [ ] `fix` — correctness fix
* [ ] `docs` — documentation / research notes
* [ ] `experiment` — experimental work
* [ ] `refactor` — structural improvement
* [ ] `test` — tests / validation
* [ ] `perf` — performance improvement
* [ ] `chore` — maintenance
* [ ] `ci` — CI/CD
* [ ] `build` — environment / Docker / dependencies

---

## Priority

* [ ] **P0** — Core / Critical
* [ ] **P1** — Important / Reusable
* [ ] **P2** — Analysis / Convenience
* [ ] **P3** — Experimental / Disposable

---

## Affected Area

<!-- Example: labs/01_attention_is_all_you_need -->

```text
```

---

## Skills Used

<!-- List relevant Agent Skills, if applicable. -->

```text
Example:

research-paper
thai-technical-explainer
research-lab-notebook
pytorch-research
benchmarking
```

---

# Research Context

## Research Question

<!-- What question is this work trying to answer? -->

## Hypothesis

<!-- Required for meaningful experiments. Use N/A when not applicable. -->

## Baseline

<!-- What is this compared against? -->

## Evidence

<!-- What was actually observed? Do not mix interpretation into this section. -->

## Interpretation

<!-- What might the evidence mean? -->

## Limitations

<!-- Hardware, dataset, model size, runtime, reproduction level, etc. -->

---

# Notebook Checklist

For notebook changes:

* [ ] Notebook has a clear objective.
* [ ] Learning Objectives are defined where appropriate.
* [ ] Prerequisites are documented.
* [ ] Important equations are explained.
* [ ] Important tensor shapes are documented.
* [ ] Hidden execution state is avoided.
* [ ] Notebook has been tested from a clean kernel.
* [ ] Large unnecessary outputs were removed.
* [ ] Findings and interpretations are separated.
* [ ] Limitations are documented.

If no notebooks changed:

* [ ] N/A

---

# Reproducibility

* [ ] Relevant random seeds are documented.
* [ ] Dependency changes are reflected in `pyproject.toml` / `uv.lock`.
* [ ] Important model/dataset configuration is documented.
* [ ] Hardware requirements are documented where relevant.
* [ ] Benchmark configuration is documented where relevant.

---

# Code Quality

* [ ] Code follows `CODE_STYLE.md`.
* [ ] Research work follows `RESEARCH_RULES.md`.
* [ ] Repository behavior follows `AGENTS.md`.
* [ ] Reusable code is not unnecessarily duplicated in notebooks.
* [ ] P3 experimental code is clearly identifiable.
* [ ] No secrets or credentials are included.

---

# Validation

Check completed commands:

```text
[ ] uv sync --locked
[ ] uv run ruff check .
[ ] uv run ruff format --check .
[ ] uv run pytest
[ ] docker compose config
```

Additional validation:

```text
```

---

# Dependency Changes

* [ ] No dependency changes.
* [ ] Dependencies added.
* [ ] Dependencies removed.
* [ ] Dependencies upgraded.

Reason:

```text
```

---

# Breaking Changes

* [ ] No breaking changes.
* [ ] Contains breaking changes.

Details:

---

# CHANGELOG

* [ ] `CHANGELOG.md` updated.
* [ ] Changelog update is not necessary.

---

# Screenshots / Figures

<!-- Add only when they materially help review the experiment or visualization. -->

---

# Open Questions

<!-- What remains uncertain or deserves another experiment? -->

---

# Reviewer Focus

<!-- Tell the reviewer what deserves the most attention. -->

---

## Final Check

* [ ] This PR contains one coherent change or research objective.
* [ ] The branch has been updated against `main`.
* [ ] I reviewed the final diff.
* [ ] I understand the evidence supporting the conclusions.
* [ ] The work is ready for review.
