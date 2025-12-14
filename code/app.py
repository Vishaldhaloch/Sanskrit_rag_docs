# app.py
from rag_pipeline import SanskritRAG

def main():
    rag = SanskritRAG()

    print("\n=== Sanskrit RAG System (CPU Only) ===\n")

    while True:
        query = input("Ask (or type 'exit'): ").strip()

        if query.lower() == "exit":
            print("Exiting...")
            break

        if not query:
            continue

        answer = rag.ask(query)
        print("\nAnswer:\n", answer, "\n")


if __name__ == "__main__":
    main()
