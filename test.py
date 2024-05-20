# streamlit_app.py
import streamlit as st
import os
from openai import AzureOpenAI

st.write('test')
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# Azure OpenAI クライアントの作成
client = AzureOpenAI(
    azure_endpoint=st.secrets["AZURE_OPENAI_ENDPOINT"],
    api_key=st.secrets["AZURE_OPENAI_KEY"],
    api_version="2024-02-15-preview"
)
