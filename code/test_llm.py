from llama_cpp import Llama

llm = Llama(
    model_path=r"E:\RAG_Sanskrit_Vishal_dhaloch_code\code\models\tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    n_ctx=512,
    n_threads=1,
    n_batch=1,
)

print(llm("नमस्ते", max_tokens=50))
