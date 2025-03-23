# run this once to generate your_index folder
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

# Example docs — replace with your real ones!
docs = [
    Document(page_content="Apple is a fruit."),
    Document(page_content="The sky is blue."),
]

embeddings = OpenAIEmbeddings()
vectordb = FAISS.from_documents(docs, embeddings)

vectordb.save_local("your_index")
