# rag_pipeline.py
import os
from loader import load_documents, load_docx
from preprocess import normalize_sanskrit, chunk_text
from retriever import BM25Retriever
from generator import LlamaGenerator

class SanskritRAG:
    def __init__(
        self,
        data_path=r"E:\RAG_Sanskrit_Vishal_dhaloch_code\data\Rag-docs.docx"
    ):
        print("Loading documents...")

        # 🔹 Handle file OR folder safely
        if os.path.isdir(data_path):
            self.raw_text = load_documents(data_path)
        elif os.path.isfile(data_path) and data_path.endswith(".docx"):
            self.raw_text = load_docx(data_path)
        else:
            raise ValueError("Invalid data path. Provide folder or .docx file.")

        print("Normalizing...")
        clean_text = normalize_sanskrit(self.raw_text)

        print("Chunking...")
        self.chunks = chunk_text(clean_text)

        print("Initializing retriever...")
        self.retriever = BM25Retriever(self.chunks)

        print("Loading LLM (CPU)...")
        self.generator = LlamaGenerator()

    def ask(self, query: str):
        clean_query = normalize_sanskrit(query)
        relevant_chunks = self.retriever.retrieve(clean_query, k=1)

        context = "\n\n".join(relevant_chunks)
        return self.generator.generate(context, clean_query)
