# preprocess.py
import re
import unicodedata

def normalize_sanskrit(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r'[^\u0900-\u097F\s।॥]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def chunk_text(text, max_chars=300):
    sentences = re.split(r'(।|॥)', text)

    chunks = []
    current = ""

    for s in sentences:
        if len(current) + len(s) <= max_chars:
            current += s
        else:
            chunks.append(current.strip())
            current = s

    if current.strip():
        chunks.append(current.strip())

    return chunks
