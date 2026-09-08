"""P1 - Reusable sinusoidal positional encoding (see lab 01 notebook 02_from_scratch.ipynb #6)."""

import numpy as np


def positional_encoding(seq_len: int, d_model: int) -> np.ndarray:
    """returns: PE [seq_len, d_model]"""
    position = np.arange(seq_len)[:, None]  # [seq_len, 1]
    dim = np.arange(d_model)[None, :]  # [1, d_model]
    angle_rates = 1.0 / np.power(10000.0, (2 * (dim // 2)) / d_model)  # [1, d_model]
    angles = position * angle_rates  # [seq_len, d_model]

    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angles[:, 0::2])
    pe[:, 1::2] = np.cos(angles[:, 1::2])
    return pe
