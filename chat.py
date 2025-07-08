import os
import requests
from embedder import embed_chunks
from vector_store import search_similar_chunks

def ask_chatbot(question, chat_history=[]):
    q_vector = embed_chunks([question])[0]
    context_chunks = search_similar_chunks(q_vector)

    context = "\n".join(context_chunks)
    history_prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])

    prompt = f"""You are a helpful and concise assistant. Avoid repeating phrases.
    Use the context below and previous conversation to answer the user's question.

Context:
{context}

Conversation history:
{history_prompt}

User: {question}
Assistant:"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "temperature": 0.7,
            "repeat_penalty": 1.2,
            "stream": False
        }
    )
    answer = response.json()["response"]
    chat_history.append({"role": "user", "content": question})
    chat_history.append({"role": "assistant", "content": answer})
    return answer.strip(), chat_history
