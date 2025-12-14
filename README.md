# Sanskrit RAG System

## Project Overview
This project demonstrates a CPU-only Retrieval-Augmented Generation (RAG) pipeline for Sanskrit text. It retrieves relevant context from Sanskrit documents and generates answers using a TinyLlama model.

---

## Folder Structure

RAG_Sanskrit_Vishal_Dhaloch/
├── code/ # Implementation scripts
├── data/ # Sample Sanskrit documents
├── report/ # Final PDF report
└── README.md # Setup and usage instructions


---

## Setup Instructions

1. **Create virtual environment (optional but recommended)**

```bash
conda create -n lang6 python=3.10
conda activate lang6

2. **Install dependencies**

    pip install -r requirements.txt
    pip install py-cpuinfo

3. Download TinyLlama model and place it in code/models/:
 
 tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

4. Run the application
  
  cd code
python app.py

5. Ask questions in Sanskrit

Type your question and press Enter. Type exit to quit.


Notes

The system uses BM25 for retrieval.

TinyLlama generates answers in Sanskrit (may be simple due to model size).

Works fully on CPU without GPU.


References

TinyLlama GGUF: Hugging Face

BM25 retriever: rank_bm25 Python package

LLM CPU inference: llama-cpp-python