
# 🤖 AI Agent with RAG + Supabase + Ollama (LLaMA3)

This is a Python-based conversational agent that can answer user questions using **Retrieval-Augmented Generation (RAG)**. It combines local LLMs (via [Ollama](https://ollama.com)), document chunking and vector search (with pgvector on Supabase), and a clean CLI chatbot interface.

---

## 🚀 Features

- ✅ Loads and splits PDF documents into context chunks
- ✅ Embeds chunks using `sentence-transformers` (`all-MiniLM-L6-v2`)
- ✅ Stores and queries embeddings using **Supabase** + `pgvector`
- ✅ Runs a local LLM (LLaMA 3 via Ollama) for generating responses
- ✅ Maintains chat history and contextual memory

---

## 📁 Project Structure

```
AI Agent Py Test/
├── chat.py              # Main chatbot logic
├── embedder.py          # PDF loading, chunking, and embedding
├── pdf_loader.py        # PDF reading helper
├── vector_store.py      # Supabase vector DB storage + search
├── main.py              # CLI entrypoint
├── manual_usuario.pdf   # User manual used for RAG
├── .env                 # Environment variables (not committed)
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works

1. **User loads a PDF** (e.g. `manual_usuario.pdf`)
2. **Text is split into chunks**
3. **Each chunk is embedded** into a vector using sentence-transformers
4. **Vectors are stored in Supabase** with pgvector
5. **At runtime**, the user asks a question via CLI
6. **Semantic search** is performed to retrieve relevant chunks
7. The **local LLM (LLaMA3)** is prompted with the retrieved context
8. The **response is streamed back** to the user with memory

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

You also need:
- [Python 3.10+]
- [Ollama](https://ollama.com) installed and running locally
- Supabase project with `pgvector` enabled

---

## 🧪 Usage

1. Create a `.env` file like:

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-secret-key
```

2. Make sure you have the LLaMA3 model running in Ollama:

```bash
ollama run llama3
```

3. Run the agent:

```bash
python main.py
```

---

## 🐳 Run with Docker

You can containerize and run the AI Agent using Docker:

### 1. 🏗️ Build the Docker image

```bash
docker build -t ai-agent-rag .
```

### 2. 🚀 Run the container

```bash
docker run --rm -it \
  --name ai-agent-rag \
  --env-file .env \
  -v "$(pwd)/manual_usuario.pdf:/app/manual_usuario.pdf" \
  ai-agent-rag
```

> ✅ This mounts your `manual_usuario.pdf` into the container and loads `.env` for Supabase credentials.

---

### 📝 Notes

- Make sure [Ollama](https://ollama.com) is installed and running locally on the **host machine** before running the container.
- If your Ollama server is not exposed by default, you may need to forward port `11434` with `-p 11434:11434`.

---

## 🧠 Example Prompt

```
You: Hola, soy Guillermo Díaz
Bot: ¡Hola Guillermo! ¿En qué puedo ayudarte hoy?
You: ¿Qué pasos debo seguir para configurar Windows 11 por primera vez?
```

---

## 📚 Tech Stack

- 🧠 Ollama + LLaMA3 (`llama3.2:latest`)
- 🔎 `sentence-transformers` for embeddings
- 🗃️ Supabase + `pgvector` for semantic search
- 🐍 Python 3.10 with `requests`, `langchain`, and more

---

## 🛡️ Notes

- The `.env` file is excluded via `.gitignore`
- Avoid pushing credentials or your PDF file if private

---

## 📌 TODOs

- [ ] Add web-based frontend (Streamlit or Gradio)
- [ ] Option to switch between OpenAI and Ollama
- [ ] Chunk and embed other file types (TXT, DOCX)

---

## ✨ Author

**Guillermo Díaz** — [LinkedIn](https://www.linkedin.com/in/gdiaza)
