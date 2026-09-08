"""P1 - Reusable multi-head attention (see lab 01 notebook 02_from_scratch.ipynb #5)."""

import numpy as np

from attention.scaled_dot_product import scaled_dot_product_attention


def multi_head_attention(
    x_q: np.ndarray,
    x_k: np.ndarray,
    x_v: np.ndarray,
    num_heads: int,
    d_model: int,
    rng: np.random.Generator,
    mask: np.ndarray | None = None,
) -> tuple[np.ndarray, list[np.ndarray]]:
    """
    x_q: [n_q, d_model]
    x_k, x_v: [n_k, d_model]
    returns: output [n_q, d_model], list of per-head weights (len num_heads, each [n_q, n_k])
    """
    assert d_model % num_heads == 0, "d_model must be divisible by num_heads"
    d_k = d_model // num_heads
    d_v = d_k

    # Random, untrained projections -- illustrative only, not learned.
    w_q = rng.normal(0, 0.1, size=(num_heads, d_model, d_k))
    w_k = rng.normal(0, 0.1, size=(num_heads, d_model, d_k))
    w_v = rng.normal(0, 0.1, size=(num_heads, d_model, d_v))
    w_o = rng.normal(0, 0.1, size=(num_heads * d_v, d_model))

    head_outputs = []
    head_weights = []
    for h in range(num_heads):
        q_h = x_q @ w_q[h]  # [n_q, d_k]
        k_h = x_k @ w_k[h]  # [n_k, d_k]
        v_h = x_v @ w_v[h]  # [n_k, d_v]
        out_h, w_h = scaled_dot_product_attention(q_h, k_h, v_h, mask=mask)
        head_outputs.append(out_h)
        head_weights.append(w_h)

    concat = np.concatenate(head_outputs, axis=-1)  # [n_q, num_heads * d_v]
    output = concat @ w_o  # [n_q, d_model]
    return output, head_weights
