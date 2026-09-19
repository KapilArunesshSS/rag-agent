from langchain_chroma import Chroma

def create_vectorstore(documents , embedding_model):
    vectorstore = chroma = Chroma.from_documents(
        documents,
        embedding=embedding_model,
        persist_directory="data/vectorstore"
    )

    print(f"Vectorstore created with {len(documents)} documents.")
    return vectorstore

def get_retriever(vectorstore):
    retriever = vectorstore.as_retriever(
        search_kwargs = {"k": 4}
    )
    print("Retriever created.")
    return retriever