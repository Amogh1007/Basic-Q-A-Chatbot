from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st

# Load .env file
load_dotenv()

# Read the key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini LLM
def get_google_response(question):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key, temperature=0.6)
    response=llm.invoke(question)
    return response

##Initialize Streamlit app
st.set_page_config(page_title="Q&A Chatbot Demo", page_icon="🤖")

st.header("Langchain Application")

input= st.text_input("Input: ",key="input")
response=get_google_response(input)

submit= st.button("Get Response")

## If the button is clicked, get the response from Google Gemini
if submit:
    st.subheader("The Response is")
    st.write(response)
