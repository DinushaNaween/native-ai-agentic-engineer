"""
Minimal Vector-Space Semantic Search Engine.

Demonstrates how vector embeddings and cosine similarity power modern
RAG retrieval and Agent tool lookup.
"""

from dataclasses import dataclass
from typing import List, Tuple
try:
    from .matrix_ops import cosine_similarity, Vector
except ImportError:
    from matrix_ops import cosine_similarity, Vector


@dataclass
class Document:
    doc_id: str
    text: str
    embedding: Vector


class MiniVectorStore:
    """In-memory vector store matching queries using cosine similarity."""
    
    def __init__(self):
        self._documents: List[Document] = []
        
    def add_document(self, doc_id: str, text: str, embedding: Vector) -> None:
        """Indexes a document with its vector representation."""
        self._documents.append(Document(doc_id=doc_id, text=text, embedding=embedding))
        
    def search(self, query_embedding: Vector, top_k: int = 3) -> List[Tuple[Document, float]]:
        """
        Calculates cosine similarity of query_embedding against all indexed document vectors
        and returns the top_k most relevant documents.
        """
        if not self._documents:
            return []
            
        scored = []
        for doc in self._documents:
            score = cosine_similarity(query_embedding, doc.embedding)
            scored.append((doc, score))
            
        # Sort descending by similarity score
        scored.sort(key=lambda item: item[1], reverse=True)
        return scored[:top_k]
