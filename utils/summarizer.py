import os
from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain_groq import ChatGroq
from langchain_core.documents import Document
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=GROQ_API_KEY, 
    model_name="llama-3.3-70b-versatile"
    )

def summarize_text(text):
    docs = [Document(page_content=text)]
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.invoke(docs)
    return summary
