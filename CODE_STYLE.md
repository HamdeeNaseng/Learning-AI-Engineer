# Code & Notebook Style Guide

> **Priority: P1 — Python, PyTorch & Jupyter Engineering Standard**

This guide defines coding conventions for the AI Lab repository.

The primary goal is readability, reproducibility, and learning value.

---

# 1. General Philosophy

Code should make the research concept easier to understand.

Prefer:

```text
clear
explicit
testable
reproducible
```

over:

```text
clever
compressed
over-abstracted
```

---

# 2. Priority Classification

Meaningful code should be classifiable as:

```text
P0 — Core / Critical
P1 — Important / Reusable
P2 — Analysis / Convenience
P3 — Experimental / Disposable
```

Example:

```python
# P0 - Core scaled dot-product attention implementation.
```

```python
# P1 - Shared benchmark helper.
```

```python
# P2 - Attention visualization utility.
```

```python
# P3 - Temporary experiment. Safe to remove.
```

P3 code must remain easy to identify and remove.

---

# 3. Python Version

The repository Python version is controlled by:

```text
.python-version
pyproject.toml
uv.lock
```

Do not depend on undocumented system Python behavior.

---

# 4. Dependency Management

Use:

```text
uv
```

Add dependencies with:

```text
uv add
```

Development dependencies:

```text
uv add --dev
```

Do not introduce another Python package manager without a justified architectural reason.

---

# 5. Formatting & Linting

Python code should pass:

```text
Ruff
```

Expected checks:

```text
formatting
imports
common bugs
unused code
modern Python syntax
```

Do not manually fight the formatter.

---

# 6. Naming

Use descriptive names.

Preferred:

```text
attention_scores
sequence_length
hidden_size
num_attention_heads
key_states
query_states
```

Avoid:

```text
x1
thing
temp2
data_new
final_result2
```

Short names are acceptable when mathematically conventional:

```text
q
k
v
x
y
```

especially when their meaning is immediately clear.

---

# 7. Functions

A function should normally perform one conceptual responsibility.

Preferred:

```text
project_qkv()
compute_attention_scores()
apply_attention_mask()
compute_attention_output()
```

Avoid monolithic functions mixing:

```text
loading
training
evaluation
plotting
saving
benchmarking
```

unless the code is intentionally a small educational demonstration.

---

# 8. Type Hints

Reusable Python modules should use type hints where practical.

Notebook-only exploratory cells may be lighter.

Prefer stronger typing under:

```text
shared/src/
```

than under:

```text
experiments/scratch/
```

---

# 9. Docstrings

Reusable functions should explain:

```text
purpose
important arguments
return value
shape assumptions
non-obvious behavior
```

Do not create large docstrings that merely repeat obvious code.

---

# 10. Tensor Shape Convention

Important tensor operations should annotate shapes.

Example:

```text
x: [B, T, D]

B = batch size
T = sequence length
D = hidden dimension
```

For attention:

```text
Q: [B, H, T, D_head]
K: [B, H, T, D_head]
V: [B, H, T, D_head]
```

Shape comments should appear near architectural transformations.

---

# 11. Shape Assertions

Use shape validation when it materially improves correctness.

Particularly useful for:

```text
attention
masking
head splitting
KV cache
RoPE
GQA
MQA
MoE routing
```

Avoid excessive assertions inside hot performance paths unless they are development-only.

---

# 12. Device Handling

Do not hardcode:

```text
cuda
```

unless the experiment explicitly requires CUDA.

Prefer device-aware code.

Experiments requiring GPU should state that requirement clearly.

---

# 13. dtype Discipline

Record or explain important dtype choices.

Examples:

```text
float32
float16
bfloat16
int8
int4
```

dtype is especially important for:

```text
QLoRA
FlashAttention
training stability
memory benchmarks
inference
```

---

# 14. Random Seed

Experiments involving randomness should define a visible seed when reproducibility matters.

Avoid scattering unrelated seed values across notebook cells.

---

# 15. Imports

Notebook imports should normally appear near the beginning.

Group logically:

```text
standard library

third-party

project-local
```

Avoid repeatedly importing the same package throughout a notebook without reason.

---

# 16. Notebook Naming

Use:

```text
NN_<purpose>.ipynb
```

Examples:

```text
01_attention_math.ipynb
02_attention_from_scratch.ipynb
03_attention_pytorch.ipynb
04_attention_benchmark.ipynb
```

Avoid:

```text
test.ipynb
new.ipynb
final.ipynb
final2.ipynb
Untitled.ipynb
```

---

# 17. Notebook Cell Structure

Prefer notebooks that move through:

```text
Markdown
   ↓
Code
   ↓
Result
   ↓
Interpretation
```

Avoid large uninterrupted sequences of code cells without explanation.

---

# 18. Notebook Introduction

A substantial notebook should begin with:

```text
Title
Objective
Learning Objectives
Prerequisites
Experiment Scope
```

Where applicable also include:

```text
Hypothesis
Hardware Requirements
Expected Runtime Class
```

Do not provide fake precise runtime estimates.

Use qualitative classes such as:

```text
CPU-friendly
GPU recommended
GPU required
high-memory experiment
```

---

# 19. Markdown Language

Primary explanatory language:

```text
Thai
```

Keep technical terminology in English where it improves precision.

Example:

> KV Cache คือข้อมูล Key และ Value จาก token ก่อนหน้าที่เก็บไว้เพื่อหลีกเลี่ยงการคำนวณซ้ำระหว่าง autoregressive decoding

---

# 20. Equations

For important equations:

```text
Equation
   ↓
Variable definitions
   ↓
Thai intuition
   ↓
Tensor shapes
   ↓
Code mapping
```

Do not paste equations without explaining what the variables represent.

---

# 21. Notebook Hidden State

A committed notebook should not depend on unknown execution history.

Expected validation:

```text
Restart Kernel
      ↓
Run All
      ↓
Successful Execution
```

---

# 22. Notebook Output

Keep outputs that materially support the lab.

Examples:

```text
important chart
benchmark table
small diagnostic output
final metric
```

Avoid committing:

```text
thousands of log lines
huge tensors
progress spam
binary blobs
```

---

# 23. Large Outputs

Large benchmark results should be stored under:

```text
artifacts/
```

rather than embedded directly in notebook JSON when practical.

---

# 24. Reusable Code Extraction

Notebook code should be extracted into `shared/src/` when:

```text
it is reused
it becomes complex
it requires tests
it represents reusable infrastructure
```

Example:

```text
shared/src/
├── attention/
├── training/
├── inference/
├── benchmarks/
└── visualization/
```

---

# 25. From-Scratch Implementations

From-scratch educational implementations should optimize for conceptual clarity first.

They do not need to outperform framework kernels.

Make clear when code is:

```text
educational
reference
optimized
production-oriented
```

---

# 26. Framework Verification

When practical, compare a custom implementation against a trusted framework implementation.

Example:

```text
Custom Attention
      ↓
compare numerically
      ↓
PyTorch SDPA
```

Use appropriate numerical tolerances.

---

# 27. PyTorch Modules

Reusable neural-network components should generally use:

```text
torch.nn.Module
```

when module semantics are useful.

Simple mathematical demonstrations may remain functional.

---

# 28. Training Loops

Training loops should keep responsibilities visible:

```text
forward
loss
zero_grad
backward
optimizer step
scheduler step
metrics
```

Avoid abstraction so deep that learners cannot see the training process in foundational labs.

---

# 29. Evaluation Mode

Remember appropriate transitions:

```text
model.train()
model.eval()
```

Inference sections should normally avoid gradient tracking when gradients are unnecessary.

---

# 30. No Silent Mutation

Avoid unexpectedly mutating important experiment configuration during execution.

Prefer explicit configuration values.

---

# 31. Configuration

Experiments with many parameters should consolidate configuration.

Examples:

```text
dataclass
dictionary
JSON
YAML
```

Avoid dozens of unrelated magic values scattered across cells.

---

# 32. Magic Numbers

Important constants should have meaningful names.

Preferred:

```text
NUM_HEADS = 8
CONTEXT_LENGTH = 512
WARMUP_STEPS = 20
```

unless a number is self-evident from the mathematical expression.

---

# 33. Visualization

Every chart should answer a research question.

Charts should include:

```text
title where useful
axis labels
units
legend when needed
```

Avoid decorative plots with no analytical purpose.

---

# 34. Benchmark Code

Benchmark utilities should separate:

```text
setup
warm-up
measurement
aggregation
reporting
```

Do not include model initialization time in inference latency unless that is specifically what is being measured.

---

# 35. Error Handling

Do not hide meaningful errors with broad exception handling.

Avoid:

```text
try everything
except Exception
ignore
```

unless the experiment specifically requires recovery behavior.

---

# 36. Logging

Use concise logging.

Research output should expose useful information such as:

```text
configuration
step
loss
memory
latency
device
```

Avoid excessive logs that obscure important evidence.

---

# 37. File Responsibilities

Prefer:

```text
Notebook
=
explanation + experiment + interpretation
```

```text
shared/src
=
reusable implementation
```

```text
tests
=
correctness verification
```

```text
artifacts
=
experiment outputs
```

```text
docs
=
research and engineering reasoning
```

---

# 38. Scratch Code

Temporary work belongs under:

```text
experiments/scratch/
```

or should be marked:

```text
P3
```

Scratch work must not silently become depended upon by stable labs.

---

# 39. Testing

Reusable mathematical and model utilities should have tests when practical.

Particularly important:

```text
tensor shapes
masking
RoPE
attention
KV-cache operations
sampling
routing
```

Tests should favor small deterministic tensors.

---

# 40. Comments

Comments should explain:

```text
why
assumption
shape
trade-off
non-obvious behavior
```

Avoid comments that merely restate Python syntax.

---

# 41. Refactoring Rule

Refactor when it improves:

```text
clarity
reuse
testability
correctness
```

Do not refactor purely to increase abstraction.

---

# 42. AI-Generated Code

AI-generated code is held to the same standard as human-written code.

The agent must:

```text
understand existing architecture
use relevant skills
respect priority labels
avoid duplicate utilities
validate changes
explain important assumptions
```

Generated code must not be accepted merely because it executes once.

---

# 43. Definition of Done

Code is ready when applicable checks pass:

```text
[ ] clear purpose
[ ] correct priority classification
[ ] appropriate tensor shape reasoning
[ ] no unnecessary dependency
[ ] lint passes
[ ] tests pass
[ ] notebook runs cleanly
[ ] results are reproducible enough for the experiment
[ ] experimental code is clearly separated
```
