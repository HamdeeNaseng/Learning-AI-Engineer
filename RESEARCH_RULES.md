# Research Rules

> **Priority: P1 — Research Integrity & Experiment Standard**

This document defines the research methodology for the AI Lab repository.

The goal is not merely to reproduce model outputs.

The goal is to understand:

```text
Question
   ↓
Theory
   ↓
Hypothesis
   ↓
Implementation
   ↓
Experiment
   ↓
Evidence
   ↓
Interpretation
   ↓
Engineering Implication
   ↓
Open Question
```

---

# 1. Research Principle

Every lab should clearly separate:

```text
What the paper says
        ≠
What the experiment shows
        ≠
What we interpret
        ≠
What we hypothesize
```

Never collapse these categories into one statement.

---

# 2. Evidence Classification

Research notes should distinguish evidence using the following labels.

## Paper Finding

A result explicitly reported by the paper.

Preferred:

> **Paper Finding:** The authors report that...

---

## Author Claim

A conclusion or argument made by the authors.

A claim is not automatically equivalent to experimental evidence.

---

## Experimental Evidence

Evidence directly observed from experiments in this repository.

Preferred:

> **Lab Evidence:** In this reproduction, increasing sequence length from X to Y increased...

---

## Interpretation

Reasoning derived from findings or observations.

Preferred:

> **Interpretation:** One possible explanation is...

---

## Engineering Implication

A possible consequence for practical system design.

Preferred:

> **Engineering Implication:** This may influence serving architecture because...

---

## Hypothesis

A statement that still requires testing.

Preferred:

> **Hypothesis:** GQA may reduce KV-cache memory while preserving most of the quality benefits of MHA.

---

# 3. Source Priority

When studying research, prefer sources approximately in this order:

```text
Original Paper
      ↓
Official Repository
      ↓
Author / Organization Documentation
      ↓
Reproduction Paper
      ↓
Independent Technical Analysis
      ↓
Secondary Article / Blog
```

Do not rely on summaries when the original paper is available.

Secondary sources may help explain the concept but should not silently replace primary evidence.

---

# 4. Paper Reading Workflow

Before implementation, identify:

```text
Problem
Contribution
Architecture
Key Equations
Training Setup
Dataset
Evaluation
Baselines
Results
Limitations
Assumptions
```

Then ask:

```text
What changed compared with previous work?

Why might that change matter?

What is required to reproduce it?

Which claims can realistically be tested in this lab?
```

---

# 5. Learning Objectives

Every major lab should state Learning Objectives.

Example:

```text
After this lab, the reader should be able to:

- explain Scaled Dot-Product Attention
- derive its tensor shapes
- implement it with PyTorch primitives
- compare it with PyTorch SDPA
- explain why scaling by sqrt(d_k) exists
```

Learning Objectives should describe capabilities, not topics.

Avoid:

```text
Learn Attention
Learn Transformers
```

Prefer:

```text
Implement
Explain
Compare
Measure
Analyze
Evaluate
```

---

# 6. Prerequisites

Every major topic should identify prerequisites.

Examples:

```text
Linear Algebra
Matrix Multiplication
Probability
Softmax
Gradient Descent
PyTorch Tensor Operations
Previous Lab
```

If a concept depends strongly on a previous lab, reference it explicitly.

---

# 7. Hypothesis Before Experiment

For meaningful experiments, state the hypothesis before observing the result.

Example:

```text
Hypothesis:

Increasing sequence length should increase the memory
advantage of FlashAttention relative to naive attention.
```

Avoid forming a hypothesis after seeing the result and presenting it as if it existed beforehand.

---

# 8. Experimental Variables

Identify:

```text
Independent Variable
Dependent Variable
Controlled Variables
```

Example:

```text
Independent:
sequence length

Dependent:
peak GPU memory

Controlled:
GPU
dtype
batch size
hidden dimension
number of heads
PyTorch version
```

Changing multiple important variables simultaneously makes interpretation weaker.

---

# 9. Baseline Rule

Whenever possible, compare against a meaningful baseline.

Examples:

```text
FlashAttention
vs
Standard Attention
```

```text
Muon
vs
AdamW
```

```text
GQA
vs
MHA
vs
MQA
```

```text
RAG
vs
No Retrieval
```

A benchmark without a baseline often provides little engineering information.

---

# 10. Reproduction Levels

Use one of the following classifications.

## Level 0 — Concept Demonstration

Toy example demonstrating the core mechanism.

## Level 1 — Algorithm Reproduction

Implement the main algorithm with simplified settings.

## Level 2 — Experimental Reproduction

Attempt to reproduce a subset of reported experiments.

## Level 3 — Large-Scale Reproduction

Attempt to reproduce training or evaluation at meaningful scale.

Do not describe Level 0 or Level 1 work as a full reproduction of the paper.

---

# 11. Reproducibility Metadata

Experiments should record relevant environment information.

Examples:

```text
Date
Git Commit
Python
PyTorch
CUDA
GPU
CPU
RAM
Operating System
Model
Dataset
dtype
Seed
Batch Size
Sequence Length
Learning Rate
Optimizer
Training Steps
```

Not every experiment requires every field.

Record what materially affects the result.

---

# 12. Randomness

Set seeds where randomness materially affects results.

Document when full determinism cannot be guaranteed.

Do not claim:

```text
100% deterministic
```

unless that property has actually been verified.

---

# 13. Dataset Discipline

Document:

```text
dataset name
dataset version
split
sample size
preprocessing
tokenization
filtering
```

Do not silently modify datasets between experiments.

Small sample datasets used for educational purposes should be clearly distinguished from the original research dataset.

---

# 14. Model Discipline

Document important model configuration.

Examples:

```text
hidden_size
num_layers
num_attention_heads
num_key_value_heads
vocab_size
context_length
parameter_count
dtype
```

When using pretrained models, record the exact model identifier and revision when practical.

---

# 15. Benchmark Warm-Up

Performance benchmarks should include warm-up iterations where appropriate.

Do not treat the first GPU execution as representative steady-state performance.

A benchmark should normally distinguish:

```text
Warm-Up
Measurement
Aggregation
```

---

# 16. Benchmark Metrics

Select metrics based on the question.

Examples:

## Training

```text
loss
tokens/sec
samples/sec
training time
peak VRAM
gradient norm
```

## Inference

```text
time to first token
inter-token latency
tokens/sec
requests/sec
peak VRAM
KV-cache size
```

## Retrieval

```text
Recall@K
Precision@K
MRR
nDCG
answer quality
retrieval latency
```

---

# 17. Hardware Context

Performance results must identify relevant hardware.

Avoid statements such as:

> FlashAttention is 3x faster.

Prefer:

> On this hardware and configuration, the experiment measured approximately X improvement.

Performance is a property of:

```text
Algorithm
+
Implementation
+
Runtime
+
Hardware
+
Workload
```

---

# 18. Statistical Discipline

Do not overinterpret a single measurement.

When practical:

```text
run multiple trials
calculate mean
report variation
inspect outliers
```

For lightweight educational labs, full statistical analysis may not be necessary, but uncertainty should still be acknowledged.

---

# 19. Negative Results

Negative results are valid research artifacts.

Do not delete an experiment merely because the expected improvement did not appear.

Instead document:

```text
Expected
Observed
Possible Explanation
Limitations
Next Experiment
```

Failed experiments may expose important assumptions.

---

# 20. No Cherry Picking

Do not selectively report only favorable runs.

If multiple runs materially disagree, investigate and document the variation.

---

# 21. From-Scratch Before Abstraction

For foundational topics, understand the mechanism before relying entirely on high-level APIs.

Preferred learning flow:

```text
Equation
   ↓
Tensor Operations
   ↓
Minimal Implementation
   ↓
Verification
   ↓
Framework Implementation
   ↓
Benchmark
```

---

# 22. Mathematical Validation

Important mathematical implementations should be checked using:

```text
shape validation
small deterministic input
known expected behavior
comparison with reference implementation
numerical tolerance
```

For example:

```text
custom attention
        ↓
compare
        ↓
torch scaled_dot_product_attention
```

where the comparison is technically valid.

---

# 23. Tensor Shape Documentation

Deep-learning experiments should explain major shape transformations.

Example:

```text
x
[B, T, D]

↓ projection

Q, K, V
[B, H, T, D_head]

↓ attention

scores
[B, H, T, T]

↓ weighted aggregation

output
[B, T, D]
```

Tensor shape reasoning is part of the research explanation.

---

# 24. Results vs Interpretation

Results sections should answer:

```text
What happened?
```

Interpretation sections should answer:

```text
Why might it have happened?
```

Keep them separate.

---

# 25. Engineering Interpretation

Every important lab should connect the research concept to system behavior.

Examples:

```text
RoPE
→ context representation

GQA
→ KV-cache memory

FlashAttention
→ memory bandwidth

PagedAttention
→ serving memory management

Chinchilla
→ compute allocation

LoRA
→ fine-tuning memory

Speculative Decoding
→ inference latency
```

---

# 26. Limitations

Every substantial experiment should acknowledge relevant limitations.

Examples:

```text
small dataset
toy model
single GPU
short training duration
different hardware
different tokenizer
reduced model size
synthetic data
different implementation
```

Limitations are part of the result, not an optional disclaimer.

---

# 27. Open Questions

Important labs should end with questions rather than forcing a final conclusion.

Examples:

```text
Would this behavior remain at larger model scale?

How much of the improvement comes from the algorithm
versus the optimized kernel?

At what sequence length does this optimization become useful?

Does the same trade-off hold during training and inference?
```

---

# 28. Research Artifact Structure

Prefer:

```text
labs/<topic>/

README.md

notebooks/
docs/
figures/
artifacts/
```

Store machine-readable experiment outputs under:

```text
artifacts/
```

Examples:

```text
metrics.json
benchmark.csv
config.json
environment.json
```

---

# 29. Lab Completion Criteria

A substantial lab should answer:

```text
[ ] What problem is being studied?
[ ] What does the paper propose?
[ ] What are the prerequisites?
[ ] What are the key equations?
[ ] What is the hypothesis?
[ ] What is the baseline?
[ ] What variables are controlled?
[ ] What was implemented?
[ ] What was measured?
[ ] What evidence was obtained?
[ ] What are the limitations?
[ ] What is the engineering implication?
[ ] What question should be tested next?
```

---

# 30. Final Research Principle

The repository should not merely answer:

```text
"How does this technique work?"
```

It should progressively help answer:

```text
Why was it designed this way?

Under what assumptions does it work?

What does the evidence actually support?

Where does it fail?

What changes when we put it into a real system?

What experiment should we run next?
```
