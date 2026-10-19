"""
Tests for pure Python linear algebra operations vs NumPy.
"""

import pytest
import math
import numpy as np

import sys
from pathlib import Path

# Add src to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from matrix_ops import (
    dot_product,
    vector_norm,
    cosine_similarity,
    matrix_multiply,
)
from semantic_search import MiniVectorStore


def test_dot_product():
    u = [1.0, 2.0, 3.0]
    v = [4.0, 5.0, 6.0]
    # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
    assert math.isclose(dot_product(u, v), 32.0)
    assert math.isclose(dot_product(u, v), float(np.dot(u, v)))


def test_vector_norm():
    v = [3.0, 4.0]
    # sqrt(3^2 + 4^2) = 5
    assert math.isclose(vector_norm(v), 5.0)
    assert math.isclose(vector_norm(v), float(np.linalg.norm(v)))


def test_cosine_similarity():
    u = [1.0, 0.0]
    v = [0.0, 1.0]
    # Orthogonal vectors -> cosine similarity = 0
    assert math.isclose(cosine_similarity(u, v), 0.0)
    
    # Collinear identical vectors -> cosine similarity = 1
    assert math.isclose(cosine_similarity(u, u), 1.0)
    
    # Compare with NumPy calculation
    a = [1.2, 3.4, -0.5]
    b = [2.1, 1.0, 4.2]
    expected = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    assert math.isclose(cosine_similarity(a, b), float(expected))


def test_matrix_multiply():
    A = [
        [1.0, 2.0],
        [3.0, 4.0]
    ]
    B = [
        [5.0, 6.0],
        [7.0, 8.0]
    ]
    # A x B = [[19, 22], [43, 50]]
    expected_np = np.matmul(A, B).tolist()
    result = matrix_multiply(A, B)
    
    assert len(result) == 2
    assert len(result[0]) == 2
    for i in range(2):
        for j in range(2):
            assert math.isclose(result[i][j], expected_np[i][j])


def test_semantic_search():
    store = MiniVectorStore()
    
    # Simulated 3D embeddings for demo:
    # Dimension 0: Machine Learning, Dimension 1: Food/Cooking, Dimension 2: Animals
    store.add_document("doc1", "Introduction to Neural Networks", [0.95, 0.05, 0.05])
    store.add_document("doc2", "Delicious Italian Pasta Recipe", [0.02, 0.98, 0.10])
    store.add_document("doc3", "How to Train Your Golden Retriever", [0.05, 0.10, 0.92])
    
    # Query vector close to ML: [0.90, 0.10, 0.0]
    query = [0.90, 0.10, 0.0]
    results = store.search(query, top_k=1)
    
    assert len(results) == 1
    top_doc, score = results[0]
    assert top_doc.doc_id == "doc1"
    assert score > 0.95
