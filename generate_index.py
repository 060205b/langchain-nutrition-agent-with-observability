import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document

# Load your dataset
df = pd.read_csv("data/foundation_food.csv")

# Convert each row to a Document 
docs = [
    Document(page_content=f"Meal: {row['Meal']}. Calories: {row['Calories']}. Diet: {row['Diet']}.")
    for _, row in df.iterrows()
]

# Initialize embeddings and FAISS index
embeddings = OpenAIEmbeddings()
vectordb = FAISS.from_documents(docs, embeddings)

# Save the index for later use
vectordb.save_local("your_index")

print("Index generated and saved to 'your_index' folder.")
