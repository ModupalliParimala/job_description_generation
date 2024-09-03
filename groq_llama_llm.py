"""Loading LLM"""

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def load_llm():
    """LLM Model to be used"""
    llm = ChatGroq(model="llama-3.1-70b-versatile")
    return llm
