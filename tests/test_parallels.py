"""Тестове за parallels engine."""
from __future__ import annotations

import numpy as np

from macro_satellite.analytics.parallels import (
    MACRO_SIGNATURE,
    _cosine_vector_vs_matrix,
    _n_common_per_row,
)


def test_cosine_identical_vectors():
    t = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    m = np.array([[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]])
    sims = _cosine_vector_vs_matrix(t, m)
    assert abs(sims[0] - 1.0) < 1e-9


def test_cosine_opposite_vectors():
    t = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    m = np.array([[-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0]])
    sims = _cosine_vector_vs_matrix(t, m)
    assert abs(sims[0] - (-1.0)) < 1e-9


def test_cosine_with_nan_rows():
    t = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    m = np.array([
        [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],     # identical
        [np.nan]*7,                                # all-NaN → NaN
        [1.0, 2.0, 3.0, np.nan, np.nan, np.nan, np.nan],  # only 3 common → below min=7
    ])
    sims = _cosine_vector_vs_matrix(t, m)
    assert abs(sims[0] - 1.0) < 1e-9
    assert np.isnan(sims[1])
    assert np.isnan(sims[2])  # below min common


def test_n_common_count():
    t = np.array([1.0, np.nan, 3.0, 4.0])
    m = np.array([
        [1.0, 2.0, 3.0, 4.0],     # 3 common (skip NaN slot in t)
        [np.nan, np.nan, np.nan, 4.0],  # 1 common
    ])
    n = _n_common_per_row(t, m)
    assert n[0] == 3
    assert n[1] == 1


def test_macro_signature_has_10_symbols():
    assert len(MACRO_SIGNATURE) == 10
    assert "SPY" in MACRO_SIGNATURE
    assert "GLD" in MACRO_SIGNATURE
    assert "USO" in MACRO_SIGNATURE
