import os
from dotenv import load_dotenv
load_dotenv()

from langchain.chains.question_answering import load_qa_chain
from langchain_community.llms import OpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langsmith import traceable

# Initialize LLM and embeddings
llm = OpenAI(temperature=0)  
embeddings = OpenAIEmbeddings()

# Load your FAISS vector index
vectordb = FAISS.load_local("your_index", embeddings, allow_dangerous_deserialization=True)

# Load QA chain
chain = load_qa_chain(llm, chain_type="stuff")

@traceable(name="generate_answer_chain")
def generate_answer(query: str) -> str:
    docs = vectordb.similarity_search(query)
    result = chain.run(input_documents=docs, question=query)
    return result
