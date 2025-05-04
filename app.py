from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate # initial prompt template
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model # to load groq model 

import streamlit as st 
import os
from dotenv import load_dotenv


#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Langsirth
LANGSMITH_TRACING="true"
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="<yourapikey>"
LANGSMITH_PROJECT="ChatBot"
OPENAI_API_KEY="<your-openai-api-key>"

# groq API
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")



# custom template for the Prompt
promt = ChatPromptTemplate.from_messages(
    [
        ("system","You are helpfull assistant. Please response to the user queries"),
        ('user',"Question: {question}")
    ]
)

st.title("Lanchain Chatbot")
input_text = st.text_input("Search the topic")

## groq llm
# llm = 
llm = init_chat_model("llama3-8b-8192", model_provider="groq")

output_parser = StrOutputParser()
chain = promt| llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


