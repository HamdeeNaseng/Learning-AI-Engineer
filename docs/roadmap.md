# Roadmap

Planned labs in intended reading order. Numbering is a learning sequence, not a schedule.

Legend: ✅ complete · 🚧 scaffolded · ⬜ planned

```text
labs/
│
├── ✅ 01_attention_is_all_you_need/
├── 🚧 02_bert/
├── ⬜ 03_gpt/
├── ⬜ 04_gpt2/
├── ⬜ 05_scaling_laws/
├── ⬜ 06_gpt3/
├── ⬜ 07_the_pile/
├── ⬜ 08_chinchilla/
├── ⬜ 09_palm/
├── ⬜ 10_opt/
├── ⬜ 11_bloom/
├── ⬜ 12_llama/
│
├── ⬜ 13_instructgpt/
├── ⬜ 14_constitutional_ai/
├── ⬜ 15_self_instruct/
│
├── ⬜ 16_lora/
├── ⬜ 17_qlora/
│
├── ⬜ 18_flashattention/
├── ⬜ 19_flashattention2/
├── ⬜ 20_rope/
├── ⬜ 21_alibi/
├── ⬜ 22_mqa/
├── ⬜ 23_gqa/
│
├── ⬜ 24_speculative_decoding/
├── ⬜ 25_paged_attention_vllm/
├── ⬜ 26_kv_cache_optimization/
│
├── ⬜ 27_rag/
│
├── ⬜ 28_chain_of_thought/
├── ⬜ 29_tree_of_thoughts/
├── ⬜ 30_react/
│
├── ⬜ 31_dpo/
├── ⬜ 32_orpo/
├── ⬜ 33_grpo/
│
├── ⬜ 34_switch_transformer_moe/
├── ⬜ 35_deepseek_moe/
│
├── ⬜ 36_test_time_scaling/
└── ⬜ 37_muon_optimizer/
```

Groups above are separated by blank lines: foundation models & scaling, alignment, efficient
fine-tuning, attention & positional optimization, inference optimization, retrieval, reasoning &
agents, preference optimization, mixture of experts, and frontier topics. The same grouping with
names is in the [root README](../README.md#roadmap).

## Threads that connect labs

Lab 01 already raises questions that later labs are meant to answer:

| From lab 01 | Picked up by |
|---|---|
| `O(n²·d)` cost and the `n = d` crossover | `18_flashattention`, `19_flashattention2` |
| Sinusoidal positional encoding extrapolation limits | `20_rope`, `21_alibi` |
| KV cache growth during decoding | `22_mqa`, `23_gqa`, `25_paged_attention_vllm` |
| Post-norm vs pre-norm stability at depth | any lab building a deep stack |

Full list with current status:
[`labs/01_attention_is_all_you_need/docs/open-questions.md`](../labs/01_attention_is_all_you_need/docs/open-questions.md)
