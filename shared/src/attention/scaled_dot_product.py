"""P1 - Reusable scaled dot-product attention (see lab 01 notebook 02_from_scratch.ipynb #4)."""

import numpy as np


def scaled_dot_product_attention(
    q: np.ndarray,
    k: np.ndarray,
    v: np.ndarray,
    mask: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    q: [..., n_q, d_k]
    k: [..., n_k, d_k]
    v: [..., n_k, d_v]
    mask: [..., n_q, n_k], True = masked out (optional)
    returns: output [..., n_q, d_v], weights [..., n_q, n_k]
    """
    d_k = q.shape[-1]
    scores = q @ np.swapaxes(k, -1, -2) / np.sqrt(d_k)  # [..., n_q, n_k]

    if mask is not None:
        scores = np.where(mask, -np.inf, scores)

    scores = scores - np.max(scores, axis=-1, keepdims=True)  # numerical stability
    exp_scores = np.exp(scores)
    weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)  # [..., n_q, n_k]

    output = weights @ v  # [..., n_q, d_v]
    return output, weights
