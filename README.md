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

## ⚙️ How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/GuillermoDiaz89/ai-agent-rag-supabase.git
cd ai-agent-rag-supabase
```

### 2. Set up Python environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create a `.env` file

Create a file named `.env` in the root with the following content:

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-secret-key
```

You must have a Supabase project with the `pgvector` extension enabled and a table like this:

```sql
create extension if not exists vector;
create table documents (
  id uuid primary key default gen_random_uuid(),
  content text,
  embedding vector(384)
);
```

Adjust `vector(384)` to match your embedding model output size.

### 4. Start Ollama

Make sure [Ollama](https://ollama.com) is installed and the LLaMA3 model is downloaded:

```bash
ollama run llama3
```

### 5. Run the CLI agent

```bash
python main.py
```

---

## 🧠 How It Works

1. **User loads a PDF** (e.g. `manual_usuario.pdf`)  
2. **Text is split into chunks**  
3. **Each chunk is embedded** using sentence-transformers  
4. **Embeddings are stored in Supabase** using pgvector  
5. **At runtime**, the user asks a question via CLI  
6. **Semantic search** retrieves the top relevant chunks  
7. The **local LLM (LLaMA3)** is prompted with the retrieved context  
8. The **response is streamed back** to the user  

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
- 🐍 Python 3.10 with `requests`, `langchain`, etc.

---

## 🛡️ Notes

- `.env` is excluded via `.gitignore`  
- You should avoid committing `manual_usuario.pdf` if it's confidential  

---

## 📌 TODOs

- [ ] Add web-based frontend (Streamlit or Gradio)  
- [ ] Option to switch between OpenAI and Ollama  
- [ ] Chunk and embed other file types (TXT, DOCX)

---

## ✨ Author

**Guillermo Díaz** — [LinkedIn](https://www.linkedin.com/in/gdiaza)
