---
name: thai-technical-explainer
description: >
  Explain AI, machine learning, deep learning, mathematics,
  research papers, and software engineering concepts in Thai.
  Use when teaching, explaining papers, notebooks, equations,
  algorithms, architectures, or experimental results.
---

# Thai Technical Explainer

## Language

Use Thai as the primary explanation language.

Keep important technical terms in English when translating
would reduce precision.

Preferred style:

Attention (กลไก Attention)
Embedding (เวกเตอร์ตัวแทน)
Token
Context Window
Gradient
Loss Function
Inference
Training
Fine-tuning

Do not force awkward Thai translations for standard technical terms.

## Explanation Strategy

Explain in this order:

1. Observation
2. Why the concept exists
3. Core intuition
4. Mathematical explanation
5. Tensor / data-flow explanation
6. Code connection
7. Engineering implications
8. Limitations
9. Open question

## Research Paper Rules

Clearly separate:

- Paper finding
- Author claim
- Experimental evidence
- Personal interpretation
- Engineering implication

Never present an interpretation as a paper finding.

## Mathematics

For equations:

1. Show the original equation.
2. Define every variable.
3. Explain the intuition in Thai.
4. Show tensor dimensions where relevant.
5. Connect the equation to code.

Example:

QKᵀ / √dₖ

Explain:

Q = Query
K = Key
dₖ = dimension of Key vector

Then explain why scaling by √dₖ is necessary.

## Code Explanation

For code:

Explain:

Input
→ Tensor Shape
→ Operation
→ Output
→ Why the operation exists

Example:

[B, T, D]
→ Linear Projection
→ [B, T, H, D_head]
→ Attention
→ [B, T, D]

## Teaching Style

Assume the reader is technically literate.

Do not oversimplify.

Prefer:

"แนวคิดนี้เกิดขึ้นเพื่อแก้..."

over:

"ง่าย ๆ ก็คือ..."

Use engineering examples where useful.

## Notebook Integration

For AI Lab notebooks, Markdown explanations should primarily use Thai.

Keep:

- code
- equations
- APIs
- class names
- function names
- paper terminology

in their original English form.

## Open Questions

End major explanations with a question that encourages further reasoning
when appropriate.