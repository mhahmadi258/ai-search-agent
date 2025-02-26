import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_aws import BedrockLLM
from langchain_community.tools import DuckDuckGoSearchRun
import streamlit as st

load_dotenv()

search_tool = DuckDuckGoSearchRun()

prompt = ChatPromptTemplate.from_messages([
    ('system','Summarize the provided content by user. Write a paragraph and then use exactly three bullet points.'),
    ('user','{input}'),
])

llm = BedrockLLM(
    credentials_profile_name = os.getenv("CREDENTIALS_PROFILE_NAME"),
    model_id = 'anthropic.claude-v2',
    region = 'us-east-1'
)

chain = search_tool | prompt | llm


query = st.text_input('Enter your search query here')

if st.button('Search'):
    if query:
        st.write('Searching the web and summarizing the content with AI ...')
        ai_respone = chain.invoke(query)

        st.subheader('Results')
        st.write(ai_respone)
    else:
        st.write('Please enter a search query to proceed')




