# Learning AI Engineer

An **AI Research & Engineering Lab** — a place to turn papers into understanding you can defend,
not just notebooks that run.

Each lab follows the same arc:

```text
Paper → Understanding → Mathematics → Implementation → Experiment → Measurement → Open Questions
```

> **Language:** repository conventions (this file, `AGENTS.md`, `CONTRIBUTING.md`) are in English.
> Lab explanations and notebooks are written in **Thai**, keeping standard technical terminology in
> English — see the language policy in [`AGENTS.md`](AGENTS.md).

---

## Status

| Lab | Status |
|---|---|
| [01 — Attention Is All You Need](labs/01_attention_is_all_you_need/) | ✅ **Complete** — concept → from-scratch implementation → experiment verified against `torch` → analysis |
| 02 — BERT | 🚧 Scaffolded (README only) |
| 03–37 | ⬜ Planned (see [Roadmap](#roadmap)) |

Details in [`STATUS.md`](STATUS.md).

---

## Quick Start

```bash
# 1. Set up the environment (uv is required)
uv sync

# 2. Launch Jupyter
uv run jupyter lab

# 3. Open the first lab
#    labs/01_attention_is_all_you_need/notebooks/01_concept.ipynb
```

Everything runs on CPU — no GPU required. Start with
[`labs/01_attention_is_all_you_need/README.md`](labs/01_attention_is_all_you_need/README.md),
which lays out the learning path with time estimates.

A `docker compose` setup is included for a pgvector-backed Postgres used by the retrieval labs:

```bash
cp .env.example .env
docker compose up -d db
```

---

## Repository Structure

```text
.
├── labs/                  # one directory per paper — the actual learning content
│   └── 01_attention_is_all_you_need/
│       ├── notebooks/     # concept → implementation → experiment → analysis
│       ├── docs/          # paper notes, engineering notes, limitations, open questions
│       └── media/         # figures and tables from the paper
│
├── shared/src/            # reusable code promoted out of notebooks
│   └── attention/         # scaled dot-product, multi-head, positional encoding
│
├── tests/                 # tests mirroring shared/src
├── experiments/scratch/   # throwaway experiments (P3)
├── data/  models/         # gitignored payloads; policies documented in each README
└── .agents/skills/        # installed agent skills
```

---

## Conventions

| Document | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | The repository contract — how humans and AI agents work here (skill routing, notebook rules, research methodology) |
| [`RESEARCH_RULES.md`](RESEARCH_RULES.md) | Research integrity and experiment standards |
| [`CODE_STYLE.md`](CODE_STYLE.md) | Python, PyTorch and Jupyter conventions |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution workflow and Conventional Commits |
| [`GIT_FLOW.md`](GIT_FLOW.md) | Branching model |

Two rules worth knowing up front:

- **Separate what the paper reports from what we conclude.** Write "the paper reports…", then
  separately "one engineering implication may be…" (`AGENTS.md` §19).
- **Notebooks must run top to bottom.** Restart kernel → Run All → no errors, before a lab counts as
  done (`AGENTS.md` §13).

---

## Validation

```bash
uv run ruff check .          # lint
uv run ruff format --check . # formatting
uv run pytest                # tests
uv lock --check              # lockfile is in sync
docker compose config        # compose file is valid
```

`scripts/check.ps1` (Windows) runs all of the above plus `mypy` and a Docker image build.
CI runs the same checks minus those two, and additionally validates that every notebook under
`labs/` is structurally sound — see [`.github/workflows/ci.yaml`](.github/workflows/ci.yaml).

---

## Roadmap

Planned labs, grouped by the thread they belong to. Numbering is the intended reading order, not a
schedule. Per-lab status and the threads connecting labs are in [`docs/roadmap.md`](docs/roadmap.md).

**Foundation models & scaling**
`01 attention` · `02 bert` · `03 gpt` · `04 gpt2` · `05 scaling_laws` · `06 gpt3` · `07 the_pile` ·
`08 chinchilla` · `09 palm` · `10 opt` · `11 bloom` · `12 llama`

**Alignment & instruction tuning**
`13 instructgpt` · `14 constitutional_ai` · `15 self_instruct`

**Efficient fine-tuning**
`16 lora` · `17 qlora`

**Attention & positional optimization**
`18 flashattention` · `19 flashattention2` · `20 rope` · `21 alibi` · `22 mqa` · `23 gqa`

**Inference optimization**
`24 speculative_decoding` · `25 paged_attention_vllm` · `26 kv_cache_optimization`

**Retrieval**
`27 rag`

**Reasoning & agents**
`28 chain_of_thought` · `29 tree_of_thoughts` · `30 react`

**Preference optimization**
`31 dpo` · `32 orpo` · `33 grpo`

**Mixture of Experts**
`34 switch_transformer_moe` · `35 deepseek_moe`

**Frontier**
`36 test_time_scaling` · `37 muon_optimizer`

Lab 01 already answers several questions that later labs pick up — the `n = d` complexity crossover
feeds into 18/19, positional encoding extrapolation into 20/21, and KV cache pressure into 22/23.
See [`open-questions.md`](labs/01_attention_is_all_you_need/docs/open-questions.md).

---

## License

[MIT](LICENSE)
