# Changelog

All notable changes to this repository will be documented in this file.

The repository follows a lightweight Semantic Versioning approach where practical.

---

## [Unreleased]

### Added

* Initial AI Lab repository architecture.
* Agent orchestration via `AGENTS.md`.
* Claude Code bootstrap via `CLAUDE.md`.
* Shared Python environment using `uv`.
* Docker Compose development environment.
* Research skill integration.

### Changed

### Fixed

### Experiments

### Documentation

### Removed

---

## Change Categories

Use the following categories where appropriate.

### Added

New labs, functionality, utilities, or major research material.

Example:

```text
Added RoPE from-scratch implementation.
```

### Changed

Meaningful changes to existing behavior or structure.

### Fixed

Corrections to code, equations, experiments, notebooks, or documentation.

### Experiments

New experimental results that do not yet represent stable repository functionality.

Example:

```text
Compared GQA and MQA KV-cache memory usage.
```

### Documentation

Important research notes or documentation improvements.

### Removed

Deleted deprecated, obsolete, or unsuccessful implementation paths.

---

## Versioning Guidance

### Patch

```text
0.1.0 → 0.1.1
```

Use for:

* corrections
* notebook fixes
* documentation fixes
* minor experiment improvements

### Minor

```text
0.1.0 → 0.2.0
```

Use for:

* new major lab
* new research track
* significant shared tooling

### Major

```text
0.x → 1.0.0
```

Use when the repository reaches a stable and coherent curriculum or introduces breaking structural changes.

---

## Example

```text
## [0.3.0] - 2026-09-08

### Added

- BERT masked-language-modeling lab.
- Shared tokenizer utilities.

### Experiments

- Compared learned positional embeddings with sinusoidal encoding.

### Fixed

- Corrected padding-mask broadcasting in multi-head attention.

### Documentation

- Added engineering interpretation of bidirectional pretraining.
```

---

## Rule

Do not update the changelog for every trivial edit.

Update it for changes that future readers or contributors would reasonably want to know about.
