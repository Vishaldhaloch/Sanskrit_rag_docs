# generator.py
from llama_cpp import Llama
import os

MODEL_PATH = r"E:\RAG_Sanskrit_Vishal_dhaloch_code\code\models\tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"

class LlamaGenerator:
    def __init__(self):
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

        self.llm = Llama(
            model_path=MODEL_PATH,
            n_ctx=1024,
            n_threads=1,     # 🔴 keep 1
            n_batch=1,       # 🔴 keep 1
            use_mlock=False,
            use_mmap=True,
            verbose=False
        )


    def generate(self, context, question):
    # 🔴 HARD truncate context (token-safe approximation)
        context = context[:400]

        prompt = (
            "उत्तरं केवलं संस्कृतेन लिखत।\n\n"
            "सन्दर्भः:\n"
            f"{context}\n\n"
            "प्रश्नः:\n"
            f"{question}\n\n"
            "उत्तरः:\n"
        )

        out = self.llm(prompt, max_tokens=64)  # 🔴 reduce
        return out["choices"][0]["text"].strip()



