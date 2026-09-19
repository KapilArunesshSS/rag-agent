# 🤖 RAG Agent

A Python-based **Retrieval-Augmented Generation (RAG) Agent** that allows users to ask questions about a collection of PDF documents. The system retrieves relevant document content and uses an LLM to generate context-aware answers.

## 🚀 Features

* 📄 Multiple PDF document ingestion
* ✂️ Text splitting and chunking
* 🧠 Sentence Transformer embeddings
* 🗄️ Vector database storage
* 🔎 Semantic similarity search
* 🤖 LLM-powered question answering
* 🔗 LangChain integration
* 🧩 LangGraph agent workflow
* ⚡ FastAPI backend

## 🏗️ Architecture

```text
PDFs
 │
 ▼
Document Loader
 │
 ▼
Text Splitter
 │
 ▼
Embeddings
 │
 ▼
Vector Database
 │
 └──────────────┐
                ▼
User Query → Retriever
                │
                ▼
        Relevant Chunks
                │
                ▼
              LLM
                │
                ▼
             Answer
```

## 📂 Project Structure

```text
rag-agent/
│
├── app/
│   ├── ingestion/
│   │   ├── loader.py
│   │   ├── splitter.py
│   │   ├── embedder.py
│   │   └── pipeline.py
│   │
│   ├── retrieval/
│   │   └── retriever.py
│   │
│   ├── agent/
│   │   ├── graph.py
│   │   ├── state.py
│   │   └── nodes.py
│   │
│   ├── llm/
│   │   └── model.py
│   │
│   └── main.py
│
├── data/
│   └── documents/
│
├── vectorstore/
├── notebooks/
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **LangGraph**
* **Sentence Transformers**
* **ChromaDB**
* **FastAPI**
* **LLM API**

## ⚙️ Setup

```bash
git clone https://github.com/<username>/rag-agent.git
cd rag-agent

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Add your PDF files to:

```text
data/documents/
```

Run the application:

```bash
uvicorn app.main:app --reload
```

API documentation:

```text
http://localhost:8000/docs
```

## 🎯 Goal

Build an end-to-end RAG Agent that can **ingest documents, retrieve relevant knowledge, and generate grounded answers using an LLM**.

## 👨‍💻 Author

**Kapil Arunessh**

GitHub: https://github.com/KapilArunesshSS

---

⭐ If you find this project useful, consider giving it a star!
