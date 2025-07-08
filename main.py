from dotenv import load_dotenv
load_dotenv()

# 🧪 Debug opcional para verificar si .env se cargó correctamente
import os

from pdf_loader import load_pdf
from embedder import split_text, embed_chunks
from vector_store import store_vectors
from chat import ask_chatbot


# 1. Procesar el PDF una vez
text = load_pdf("manual_usuario.pdf")
chunks = split_text(text)
vectors = embed_chunks(chunks)
store_vectors(chunks, vectors)

# 2. Preguntar al chatbot
history = []
while True:
    q = input("User: ")
    if q.lower() in ["exit", "quit"]:
        break
    answer, history = ask_chatbot(q, history)
    print("Chatbot:", answer)
