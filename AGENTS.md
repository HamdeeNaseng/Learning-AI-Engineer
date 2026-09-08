# AGENTS.md

> **Priority: P0 — Repository Agent Contract**
>
> This file defines how AI coding and research agents must operate inside this repository.

---

# 1. Repository Purpose

This repository is an **AI Research & Engineering Lab**.

Its purpose is not only to collect notebooks or summarize papers.

The repository should help transform:

```text
Research Paper
    ↓
Understanding
    ↓
Mathematical Reasoning
    ↓
Implementation
    ↓
Experiment
    ↓
Measurement
    ↓
Engineering Interpretation
    ↓
Open Questions
```

Agents must optimize for:

* technical accuracy
* reproducibility
* understanding
* experimentation
* engineering relevance
* maintainability

Do not optimize merely for producing more files or more code.

---

# 2. Primary Language

The primary explanation language is **Thai**.

Technical terminology should remain in English where appropriate.

Preferred:

```text
Attention mechanism
Embedding
Token
Context Window
Gradient
Loss Function
Inference
Training
Fine-tuning
KV Cache
Hidden State
Query / Key / Value
```

Explain the term in Thai, but do not replace standard technical terminology with unnatural translations.

Example:

> Self-Attention คือกลไกที่ทำให้แต่ละ token สามารถประเมินความสัมพันธ์กับ token อื่นใน sequence เดียวกันได้

Prefer this over forcing every technical word into Thai.

Code, APIs, equations, class names, function names, configuration keys, and paper terminology must remain in their original form.

---

# 3. Skill-First Policy

Before performing a substantial task, agents MUST determine whether an installed skill applies.

The preferred workflow is:

```text
Understand Task
      ↓
Discover Relevant Skills
      ↓
Read Skill Instructions
      ↓
Select Minimal Skill Set
      ↓
Execute
      ↓
Validate
      ↓
Document Findings
```

Skills are not optional decoration.

When an appropriate skill exists, use it.

Do not recreate a workflow manually when an installed skill already defines that workflow.

---

# 4. Skill Discovery

Installed skills are expected under locations such as:

```text
.agents/skills/
```

or equivalent agent-supported skill directories.

Before starting complex research, notebook, PyTorch, experiment, or explanation work:

1. Inspect available skills.
2. Identify skills whose description matches the task.
3. Read their `SKILL.md`.
4. Follow the relevant workflow.
5. Combine skills only when their responsibilities are complementary.

Do not invoke every available skill.

Prefer the **smallest sufficient skill set**.

---

# 5. Skill Selection Strategy

Use skills according to the task.

## Research Paper

Preferred skills:

```text
research-paper
read-research-paper
get-research-paper
paper-reading
paper-to-lab
```

Use for:

* reading papers
* extracting contributions
* identifying assumptions
* interpreting experiments
* extracting equations
* finding limitations

---

## Thai Technical Explanation

Preferred skills:

```text
thai-technical-explainer
plain-language
translate-content
```

Priority:

```text
thai-technical-explainer
        ↓
plain-language
        ↓
translate-content
```

`thai-technical-explainer` should control technical explanation style.

`plain-language` may improve readability.

`translate-content` should only be used when actual translation is needed.

Translation must not reduce technical precision.

---

## Jupyter Notebook

Preferred skills:

```text
research-lab-notebook
jupyter-notebook
```

Use whenever creating or substantially modifying:

```text
*.ipynb
```

Notebook work must be treated as a reproducible experiment, not as a scratchpad unless explicitly placed under:

```text
experiments/scratch/
```

---

## PyTorch

Preferred skills:

```text
pytorch-research
meta-pytorch/*
```

Use for:

* tensor operations
* autograd
* neural network implementation
* performance optimization
* torch.compile
* profiling
* GPU execution
* training loops
* model implementation

Prefer PyTorch-native implementations unless the experiment specifically requires another framework.

---

## Mathematics

Preferred skill:

```text
math-explainer
```

When explaining equations, always map:

```text
Equation
   ↓
Variables
   ↓
Intuition
   ↓
Tensor Shape
   ↓
Operation
   ↓
Code
```

Do not explain mathematical notation independently from implementation when the concept is intended for engineering use.

---

## Visualization

Preferred skills:

```text
data-visualization
matplotlib
```

Routing:

```text
Visualization Task
      ↓
data-visualization
      ↓
choose correct visual representation
      ↓
matplotlib
      ↓
implement scientific visualization
      ↓
thai-technical-explainer
      ↓
explain what the figure means
```

`data-visualization` decides the right chart for the data (trend → line, comparison → bar,
distribution → histogram/box plot, correlation → scatter/heatmap) and applies accessibility/design
principles. `matplotlib` implements it — scientific plots, heatmaps, multi-panel figures, export to
PNG/PDF/SVG, and `%matplotlib widget` / `ipympl` for interactive Jupyter. `thai-technical-explainer`
then explains what the resulting figure shows, per the [Thai Technical Explanation](#thai-technical-explanation) rules.

Examples:

```text
visualize attention matrix
```

```text
matplotlib
+
thai-technical-explainer
```

```text
compare FlashAttention latency across sequence lengths
```

```text
benchmarking
+
data-visualization
+
matplotlib
+
thai-technical-explainer
```

```text
visualize RoPE rotation
```

```text
math-explainer
+
matplotlib
+
thai-technical-explainer
```

For tabular experiment results (metrics, correlation, distribution, time series, regression,
benchmark analysis) that need both statistics and charts, prefer `data-analysis` instead of
composing `matplotlib` by hand.

---

## Experiment Design

Preferred skills:

```text
ml-experiment-design
research-reproducibility
benchmarking
```

Use when:

* comparing architectures
* comparing hyperparameters
* testing hypotheses
* benchmarking performance
* performing ablations
* evaluating training or inference behavior

---

## Review

Preferred skills:

```text
notebook-reviewer
research-note-writer
```

Use before considering a lab complete.

---

# 6. Multi-Skill Composition

Skills should be composed intentionally.

Example for studying a new paper:

```text
read-research-paper
        ↓
thai-technical-explainer
        ↓
math-explainer
        ↓
paper-to-lab
        ↓
research-lab-notebook
        ↓
pytorch-research
        ↓
ml-experiment-design
        ↓
research-reproducibility
        ↓
notebook-reviewer
```

Not every task requires the entire pipeline.

Example:

> Explain RoPE mathematically in Thai.

Use approximately:

```text
thai-technical-explainer
+
math-explainer
```

Example:

> Implement FlashAttention experiment.

Use approximately:

```text
research-lab-notebook
+
pytorch-research
+
benchmarking
+
research-reproducibility
```

---

# 7. Avoid Skill Overlap

Do not stack multiple skills that perform the same responsibility unless necessary.

Bad:

```text
translation-skill-A
translation-skill-B
translation-skill-C
thai-technical-explainer
```

Preferred:

```text
thai-technical-explainer
+
translate-content   # only if translation is actually needed
```

Skills should form a pipeline, not compete for control.

---

# 8. Skill Precedence

When skill instructions conflict, use the following precedence:

```text
Repository AGENTS.md
        ↓
Task-specific instructions
        ↓
Specialized Skill
        ↓
General Skill
        ↓
Default agent behavior
```

For example:

```text
thai-technical-explainer
```

takes precedence over a generic writing skill for technical explanations.

A PyTorch-specific skill takes precedence over generic Python recommendations when working with PyTorch internals.

---

# 9. Repository Structure

Expected structure:

```text
ai-lab/
│
├── AGENTS.md
├── README.md
├── STATUS.md
│
├── pyproject.toml
├── uv.lock
├── .python-version
│
├── Dockerfile
├── compose.yaml
│
├── .agents/
│   └── skills/
│
├── labs/
│   ├── 01_attention_is_all_you_need/
│   ├── 02_bert/
│   ├── 03_gpt/
│   └── ...
│
├── shared/
│   └── src/
│
├── data/
├── models/
├── docs/
├── experiments/
│   └── scratch/
│
└── tests/
```

Agents must respect this structure.

Do not create miscellaneous files in the repository root without a clear architectural reason.

---

# 10. Lab Structure

Each research topic should normally follow:

```text
labs/<topic>/
│
├── README.md
│
├── notebooks/
│   ├── 01_concept.ipynb
│   ├── 02_from_scratch.ipynb
│   ├── 03_experiment.ipynb
│   └── 04_analysis.ipynb
│
├── docs/
│   ├── paper-notes.md
│   ├── engineering-notes.md
│   ├── limitations.md
│   └── open-questions.md
│
├── figures/
│
└── artifacts/
```

Not every topic needs every file.

Do not generate empty boilerplate files merely to satisfy structure.

Create files when they have meaningful content.

---

# 11. Notebook Philosophy

A notebook should primarily contain:

```text
Explanation
+
Experiment
+
Visualization
+
Interpretation
```

A notebook should NOT become the long-term application codebase.

If code becomes reusable, move it into:

```text
shared/src/
```

Rule:

> If meaningful implementation logic is reused for a second experiment, consider extracting it from the notebook.

---

# 12. Notebook Structure

A research notebook should normally contain:

## 1. Objective

What are we trying to understand?

## 2. Prerequisites

What knowledge is assumed?

## 3. Hypothesis

What behavior do we expect?

## 4. Theory

Explain the relevant concept.

## 5. Mathematics

Explain important equations.

## 6. Implementation

Implement the minimal required system.

## 7. Experiment

Run controlled experiments.

## 8. Results

Present measurements.

## 9. Interpretation

Explain what the results may indicate.

## 10. Limitations

Identify weaknesses in the experiment.

## 11. Engineering Implications

Connect the result to real systems.

## 12. Open Questions

Identify what deserves further investigation.

---

# 13. No Hidden Notebook State

Notebooks must be executable from top to bottom.

Do not rely on variables created by cells executed in an unknown order.

Before considering a notebook complete:

```text
Restart Kernel
      ↓
Run All
      ↓
Verify No Errors
```

Execution order must be deterministic where practical.

---

# 14. Reproducibility

Experiments should capture relevant metadata.

Examples:

```text
Python version
PyTorch version
CUDA version
GPU
random seed
dataset
model
hyperparameters
batch size
sequence length
dtype
device
```

When randomness matters, explicitly set seeds.

Example:

```python
# P1 - Reproducibility
import random

import numpy as np
import torch

SEED = 42

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)

if torch.cuda.is_available():
    torch.cuda.manual_seed_all(SEED)
```

Do not claim complete determinism unless it has actually been established.

---

# 15. Code Priority Labels

All meaningful code additions or modifications should be classifiable using:

```text
P0 — Core / Critical
P1 — Important / Reusable
P2 — Convenience / Analysis
P3 — Experimental / Disposable
```

Examples:

```python
# P0 - Core implementation of scaled dot-product attention.
```

```python
# P1 - Reusable benchmark utility.
```

```python
# P2 - Visualization helper.
```

```python
# P3 - Temporary ablation experiment. Safe to remove.
```

P3 code must be easy to identify and remove later.

Avoid spreading experimental code into production-quality shared modules.

---

# 16. From-Scratch Rule

For foundational concepts, prefer implementing the core algorithm from basic operations before using high-level abstractions.

Example:

For Attention, first understand:

```text
Q
K
V
↓
QKᵀ
↓
scale
↓
softmax
↓
weighted sum of V
```

before replacing it with:

```python
torch.nn.functional.scaled_dot_product_attention(...)
```

Libraries may be used afterward for verification and comparison.

---

# 17. Equation-to-Code Rule

Whenever a major equation is discussed, connect it to code.

Example:

```text
Attention(Q, K, V)
=
softmax(QKᵀ / √dₖ)V
```

Explanation should include:

```text
Q shape
K shape
V shape
      ↓
matrix multiplication
      ↓
attention score shape
      ↓
softmax dimension
      ↓
output shape
```

Then show the corresponding implementation.

---

# 18. Tensor Shape Discipline

For deep learning code, agents should reason explicitly about tensor shapes.

Preferred annotations:

```python
# x: [batch, seq_len, hidden_dim]
```

Transformation explanations should use:

```text
[B, T, D]
    ↓
Linear Projection
    ↓
[B, T, H, D_head]
    ↓
Attention
    ↓
[B, T, D]
```

Shape mismatches should be treated as architectural problems, not merely runtime errors.

---

# 19. Paper Findings vs Interpretation

Agents MUST separate:

```text
Paper Finding
Author Claim
Experimental Evidence
Interpretation
Engineering Implication
Hypothesis
```

Never write:

> The paper proves that...

unless the evidence genuinely supports such wording.

Prefer:

> The paper reports...

Then separately:

> One engineering implication may be...

---

# 20. Research Explanation Style

Do not merely summarize papers.

For important concepts, explain:

```text
Why does it exist?
What problem does it solve?
What assumption does it make?
How does it work?
What does the evidence show?
Where can it fail?
What changes in real systems?
```

A good lab should leave the reader with both:

```text
"I understand how this works."
```

and:

```text
"I understand why an engineer might care."
```

---

# 21. Thai Explanation Style

Thai explanations should be professional, technical, and natural.

Avoid excessive simplification such as:

> ง่าย ๆ ก็คือ...

when it removes important details.

Prefer:

> แนวคิดหลักคือ...

or:

> เหตุผลที่กลไกนี้ถูกออกแบบขึ้นมาคือ...

Use metaphors only when they improve technical understanding.

Do not use metaphor as a substitute for mathematical or architectural explanation.

---

# 22. Experiment Discipline

Every meaningful experiment should identify:

```text
Question
Hypothesis
Independent Variable
Controlled Variables
Metrics
Result
Interpretation
Limitations
```

Avoid:

```text
change several parameters
→ run model
→ observe number
→ conclude architecture is better
```

Prefer controlled comparisons.

---

# 23. Benchmark Discipline

When benchmarking performance:

Include warm-up where appropriate.

Measure relevant metrics such as:

```text
latency
throughput
tokens/sec
samples/sec
VRAM
RAM
FLOPs
training time
inference time
```

Do not compare results across substantially different hardware without noting the hardware difference.

Separate:

```text
algorithmic improvement
```

from:

```text
hardware/runtime optimization
```

---

# 24. Visualization

Visualizations must answer a question.

Avoid creating charts purely for decoration.

Good examples:

```text
attention heatmap
loss curve
scaling curve
memory usage
latency vs sequence length
tokens/sec vs batch size
position similarity
gradient magnitude
```

Always label axes and units.

Interpret what the graph means.

---

# 25. Dependency Management

This repository uses:

```text
uv
+
pyproject.toml
+
uv.lock
```

as the dependency management standard.

Do not introduce additional dependency managers without a justified reason.

Avoid unnecessary parallel dependency files such as:

```text
requirements.txt
Pipfile
poetry.lock
environment.yml
```

unless required for interoperability.

---

# 26. Environment

Preferred local development:

```text
VS Code
+
.venv
+
uv
+
Jupyter
```

Preferred reproducible environment:

```text
Docker
+
Docker Compose
```

The environment should be reconstructable from repository configuration.

Do not commit:

```text
.venv/
```

Do commit:

```text
pyproject.toml
uv.lock
.python-version
```

---

# 27. New Dependencies

Before adding a dependency:

Ask internally:

1. Is it necessary?
2. Is equivalent functionality already available?
3. Is it only needed by one experimental notebook?
4. Is the package maintained?
5. Will it introduce CUDA or platform compatibility problems?

Prefer minimal dependencies.

Do not install large AI frameworks merely because they may be useful later.

---

# 28. Dataset Policy

Do not commit large datasets into Git.

Expected:

```text
data/
├── README.md
├── raw/
├── processed/
└── sample/
```

Small reproducible samples may be committed.

Large datasets should be downloaded or generated through documented procedures.

---

# 29. Model Artifact Policy

Do not commit large model weights.

Examples:

```text
*.pt
*.pth
*.ckpt
*.bin
*.safetensors
```

Store instructions for obtaining the model instead.

Small synthetic artifacts used specifically for tests may be exceptions.

---

# 30. Scratch Experiments

Temporary experiments belong under:

```text
experiments/scratch/
```

or should clearly carry:

```text
P3
```

status.

Scratch experiments should not silently become architectural dependencies.

If an experiment becomes valuable:

```text
P3 experiment
      ↓
validate
      ↓
refactor
      ↓
P1 reusable implementation
```

---

# 31. Validation Before Completion

Before marking work complete, use the relevant validation.

For Python:

```bash
uv run ruff check .
```

For tests:

```bash
uv run pytest
```

For environment:

```bash
uv sync --locked
```

For Docker Compose:

```bash
docker compose config
```

For notebooks:

```text
Restart Kernel
→ Run All
→ Confirm clean execution
```

Use additional validation required by relevant skills.

---

# 32. Definition of Done — Research Lab

A lab is not complete merely because the notebook runs.

A mature lab should answer:

```text
[ ] What problem does the paper address?

[ ] Why was this approach proposed?

[ ] What are the main equations?

[ ] What do tensor shapes look like?

[ ] Can the core idea be implemented?

[ ] Has an experiment been performed?

[ ] Are results measurable?

[ ] Are findings separated from interpretation?

[ ] Are limitations documented?

[ ] Are engineering implications discussed?

[ ] Are open questions identified?

[ ] Can the notebook run from top to bottom?
```

---

# 33. Skill Improvement Loop

If the same workflow is repeated several times, agents should consider whether it belongs in a reusable skill.

Pattern:

```text
Repeated Manual Instruction
        ↓
Stable Workflow
        ↓
Create / Improve SKILL.md
        ↓
Reuse Across Labs
```

Examples:

```text
paper-to-lab
attention-visualization
llm-benchmarking
thai-technical-explainer
```

Do not create a skill for one-off trivial behavior.

A skill should encode reusable expertise.

---

# 34. When to Create a New Skill

Create or propose a new skill when:

* the workflow repeats across multiple labs
* specialized expertise is required
* mistakes repeatedly occur in the same area
* a validation procedure should be standardized
* several agents need the same instructions

Do NOT create:

```text
bert-skill
gpt2-skill
llama-skill
```

merely to store knowledge about individual papers.

Paper-specific knowledge belongs under:

```text
labs/<topic>/
```

Skills should represent reusable methods.

---

# 35. Good Skill Granularity

Preferred:

```text
paper-reading
paper-to-lab
math-explainer
pytorch-research
ml-experiment-design
benchmarking
research-reproducibility
thai-technical-explainer
notebook-reviewer
```

Avoid overly broad skills such as:

```text
do-ai
research-everything
machine-learning
```

Avoid excessively narrow skills unless the workflow truly requires specialized expertise.

---

# 36. Agent Decision Pattern

For every substantial task, reason operationally using:

```text
TASK
 ↓
What outcome is required?
 ↓
Which skill owns this responsibility?
 ↓
What supporting skill is needed?
 ↓
What repository files are relevant?
 ↓
What validation proves completion?
 ↓
Execute
```

Example:

```text
Task:
Implement RoPE lab

Primary Skill:
pytorch-research

Supporting:
math-explainer
research-lab-notebook
research-reproducibility

Validation:
tensor shape checks
numerical checks
notebook Run All
```

---

# 37. Avoid Unnecessary Work

Agents should not:

* create unnecessary abstractions
* create empty documentation files
* add unused dependencies
* over-engineer toy experiments
* add infrastructure unrelated to the current lab
* rewrite working code without benefit
* duplicate shared utilities
* generate large amounts of prose that do not improve understanding

Prefer minimal implementations that clearly reveal the concept.

---

# 38. Preserve Learning Value

Do not hide foundational concepts behind high-level libraries too early.

Bad learning flow:

```text
pip install library
↓
call library
↓
print output
```

Preferred:

```text
understand concept
↓
implement minimal version
↓
inspect intermediate values
↓
verify behavior
↓
compare with library implementation
```

---

# 39. Engineering Connection

Each important topic should eventually answer:

> Why should an AI Engineer, Software Engineer, or Research Engineer care about this?

Examples:

FlashAttention:

```text
Algorithm
   ↓
Memory access behavior
   ↓
GPU efficiency
   ↓
sequence length
   ↓
training/inference throughput
```

Chinchilla:

```text
Scaling law
   ↓
compute allocation
   ↓
model size vs token count
   ↓
training budget decisions
```

PagedAttention:

```text
KV cache
   ↓
memory fragmentation
   ↓
serving architecture
   ↓
batching efficiency
   ↓
LLM throughput
```

---

# 40. Final Principle

The purpose of skills in this repository is not to make the agent produce more output.

Skills exist to make the agent apply **better reasoning, stronger methodology, and more consistent engineering discipline**.

The preferred transformation is:

```text
Agent without Skills
        ↓
"Generate an Attention notebook"

Agent with Skills
        ↓
Read Paper
        ↓
Understand Mathematics
        ↓
Explain in Thai
        ↓
Implement from Scratch
        ↓
Validate Tensor Shapes
        ↓
Design Experiment
        ↓
Measure
        ↓
Interpret
        ↓
Document Limitations
        ↓
Raise New Questions
```

That is the expected behavior of agents operating in this repository.
