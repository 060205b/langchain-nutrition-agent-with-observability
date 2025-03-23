from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

# Dummy example: list of documents
docs = ["LangChain is amazing!", "FastAPI is fast", "Python is cool"]
embeddings = OpenAIEmbeddings()
db = FAISS.from_texts(docs, embeddings)

# Save it to a folder
db.save_local("your_index")

print("Index generated and saved to 'your_index' folder.")
