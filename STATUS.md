# Status

## Current State

Repository scaffolding is set up: environment, tooling, and lab/shared
structure are in place. `uv` is installed and `uv.lock` is generated.

## Labs

| Lab | Status |
|---|---|
| 01 — Attention Is All You Need | Core pipeline complete: concept → from-scratch implementation → experiment (verified against `torch`) → analysis. Reusable code extracted to `shared/src/attention/`. Training/full encoder-decoder reproduction out of scope for now. |
| 02 — BERT | Not started (README scaffolded) |

## Next Steps

- Fill in `labs/01_attention_is_all_you_need/README.md` paper metadata.
- Start `labs/02_bert`.
- Decide whether lab 01 should grow an encoder/decoder + training notebook,
  or stay scoped to the attention building blocks it currently covers.
