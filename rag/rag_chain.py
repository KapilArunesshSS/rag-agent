from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def create_rag_chain(llm, retriever):

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful AI assistant.

Answer the question using ONLY the provided context.

Rules:
- Give only one answer.
- Do not repeat the answer.
- Do not repeat the word "Answer".
- Keep the answer concise.
- If the answer is not present in the context, say:
  "I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    def retrieve_context(question):

        documents = retriever.invoke(question)

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        return context

    rag_chain = (
        {
            "context": retrieve_context,
            "question": lambda x: x
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain