import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_mcqs(summary_text, num_questions, topic=None):
    with open("prompts/mcq_prompt.txt") as f:
        template = f.read()

    prompt = PromptTemplate(
        input_variables=["context", "num_questions", "topic"],
        template=template,
    )

    llm = ChatGroq(api_key=GROQ_API_KEY, model_name="llama-3.3-70b-versatile")
    chain = prompt | llm | StrOutputParser()

    result = chain.invoke({
        "context": summary_text,
        "num_questions": num_questions,
        "topic": topic or ""
    })
    
    return result  
