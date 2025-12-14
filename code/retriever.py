# retriever.py
from rank_bm25 import BM25Okapi

class BM25Retriever:
    def __init__(self, chunks):
        self.chunks = chunks
        self.tokenized = [chunk.split() for chunk in chunks]
        self.bm25 = BM25Okapi(self.tokenized)

    def retrieve(self, query, k=3):
        tokenized_query = query.split()
        scores = self.bm25.get_scores(tokenized_query)
        top_k = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        return [self.chunks[i] for i in top_k]
