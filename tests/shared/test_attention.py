"""P1 - Correctness checks for shared/src/attention, mirroring lab 01 notebook 02."""

import numpy as np

from attention import multi_head_attention, positional_encoding, scaled_dot_product_attention


def test_scaled_dot_product_attention_matches_hand_worked_example() -> None:
    q = np.array([[1.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0]])
    k = np.array([[1.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0], [1.0, 1.0, 0.0, 0.0]])
    v = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

    output, weights = scaled_dot_product_attention(q, k, v)

    assert np.allclose(weights[0], [0.506, 0.186, 0.307], atol=1e-3)
    assert np.allclose(weights.sum(axis=-1), 1.0)
    assert output.shape == (2, 3)


def test_multi_head_attention_output_shape_independent_of_head_count() -> None:
    rng = np.random.default_rng(42)
    n, d_model = 6, 16
    x = rng.normal(size=(n, d_model))

    for h in (1, 2, 4, 8):
        output, head_weights = multi_head_attention(x, x, x, num_heads=h, d_model=d_model, rng=rng)
        assert output.shape == (n, d_model)
        assert len(head_weights) == h
        assert head_weights[0].shape == (n, n)


def test_positional_encoding_boundary_values() -> None:
    pe = positional_encoding(seq_len=4, d_model=8)
    assert pe.shape == (4, 8)
    assert np.allclose(pe[0, 0::2], 0.0)  # sin(0) = 0
    assert np.allclose(pe[0, 1::2], 1.0)  # cos(0) = 1
