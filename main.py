from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

from rag.ingestion import process_pdf, split_documents
from rag.embeddings import get_embeddings
from rag.retriever import create_vectorstore, get_retriever
from rag.rag_chain import create_rag_chain


# -------------------------
# 1. Load PDFs
# -------------------------
documents = process_pdf("data/documents")


# -------------------------
# 2. Split documents
# -------------------------
chunks = split_documents(documents)


# -------------------------
# 3. Load embedding model
# -------------------------
embedding_model = get_embeddings()


# -------------------------
# 4. Create vector database
# -------------------------
vectorstore = create_vectorstore(
    chunks,
    embedding_model
)


# -------------------------
# 5. Create retriever
# -------------------------
retriever = get_retriever(vectorstore)


# -------------------------
# 6. Load Hugging Face LLM
# -------------------------
pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen3-0.6B",
    max_new_tokens=128,
    do_sample=False,
    repetition_penalty=1.1,
    no_repeat_ngram_size=3,
    return_full_text=False,
)

llm = HuggingFacePipeline(
    pipeline=pipe
)


# -------------------------
# 7. Create RAG chain
# -------------------------
rag_chain = create_rag_chain(
    llm,
    retriever
)


# -------------------------
# 8. Ask question
# -------------------------
question = input("\nAsk a question: ")

answer = rag_chain.invoke(question)


print("\n========== ANSWER ==========\n")
print(answer)