"""
Linear Algebra Operations from Scratch.

Implemented in pure Python (without NumPy) to build intuition for:
- Vector Dot Product
- Vector Norm (Magnitude)
- Cosine Similarity
- Matrix Multiplication (2D)
"""

import math
from typing import List

Vector = List[float]
Matrix = List[List[float]]


def dot_product(u: Vector, v: Vector) -> float:
    """
    Computes the dot product of two 1D vectors u and v.
    Formula: u · v = sum(u_i * v_i) for i in range(len(u))
    """
    if len(u) != len(v):
        raise ValueError(f"Vector dimensions must match: len(u)={len(u)}, len(v)={len(v)}")
    
    return sum(x * y for x, y in zip(u, v))


def vector_norm(v: Vector) -> float:
    """
    Computes the Euclidean L2-norm (magnitude) of vector v.
    Formula: ||v|| = sqrt(sum(v_i^2))
    """
    if not v:
        raise ValueError("Cannot compute norm of empty vector")
    return math.sqrt(sum(x ** 2 for x in v))


def cosine_similarity(u: Vector, v: Vector) -> float:
    """
    Computes the cosine similarity between two vectors.
    Formula: sim(u, v) = (u · v) / (||u|| * ||v||)
    Range: [-1.0, 1.0] where 1.0 is identical direction, 0 is orthogonal.
    """
    norm_u = vector_norm(u)
    norm_v = vector_norm(v)
    
    if norm_u == 0.0 or norm_v == 0.0:
        raise ValueError("Cannot compute cosine similarity with zero-magnitude vector")
    
    return dot_product(u, v) / (norm_u * norm_v)


def matrix_shape(A: Matrix) -> tuple[int, int]:
    """Returns (rows, cols) of a 2D matrix."""
    if not A or not isinstance(A, list):
        raise ValueError("Invalid matrix")
    rows = len(A)
    cols = len(A[0]) if rows > 0 and isinstance(A[0], list) else 0
    return rows, cols


def matrix_multiply(A: Matrix, B: Matrix) -> Matrix:
    """
    Computes matrix multiplication C = A x B from scratch.
    
    A has shape (m, k)
    B has shape (k, n)
    Result C has shape (m, n)
    
    C[i][j] = sum(A[i][k] * B[k][j])
    """
    m, k_a = matrix_shape(A)
    k_b, n = matrix_shape(B)
    
    if k_a != k_b:
        raise ValueError(
            f"Inner matrix dimensions must match: A is ({m}x{k_a}), B is ({k_b}x{n})"
        )
    
    # Initialize m x n result matrix with zeros
    C: Matrix = [[0.0 for _ in range(n)] for _ in range(m)]
    
    # Standard 3-loop matrix multiplication O(m * k * n)
    for i in range(m):
        for j in range(n):
            total = 0.0
            for k in range(k_a):
                total += A[i][k] * B[k][j]
            C[i][j] = total
            
    return C
