# imports
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

#process pdf files in a folder and return a list of documents
def process_pdf (folder_path : str):

    documents = []

    pdf_docs = list(Path(folder_path).glob("*.pdf"))

    if not pdf_docs:
        print(f"No PDF files found in the folder: {folder_path}")
        return []
    
    for pdf in pdf_docs:
        print(f"Loading PDF: {pdf.name}")
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())
        for doc in documents:
            doc.metadata['source_file'] = pdf.name
            doc.metadata['file_type'] = 'pdf'
            
    print(f"Total documents loaded: {len(documents)}")
    return documents

# Splitting the documents into chunks
def split_documents(documents, chunk_size=1000, chunk_overlap=200):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )

    chunks = []
    for doc in documents:
        chunks.extend(text_splitter.split_documents([doc]))

    print(f"Total chunks created: {len(chunks)}")
    return chunks

    


