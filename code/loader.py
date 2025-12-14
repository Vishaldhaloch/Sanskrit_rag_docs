# loader.py
import os
import docx

def load_docx(path: str) -> str:
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

def load_text_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_documents(path: str) -> str:
    """
    Accepts:
    - Folder path containing .docx / .txt files
    - OR a single .docx / .txt file
    """
    full_corpus = ""

    # ✅ Case 1: single file
    if os.path.isfile(path):
        if path.endswith(".docx"):
            return load_docx(path)
        elif path.endswith(".txt"):
            return load_text_file(path)
        else:
            raise ValueError("Unsupported file type")

    # ✅ Case 2: folder
    if os.path.isdir(path):
        for file in os.listdir(path):
            file_path = os.path.join(path, file)

            if file.endswith(".docx"):
                full_corpus += load_docx(file_path) + "\n"
            elif file.endswith(".txt"):
                full_corpus += load_text_file(file_path) + "\n"

        return full_corpus.strip()

    raise ValueError("Invalid path provided")
