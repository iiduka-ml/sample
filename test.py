# streamlit_app.py
import streamlit as st

st.write('test')
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("例:", st.secrets["AZURE_OPENAI_ENDPOINT"])
st.write("例:", st.secrets["AZURE_OPENAI_API_KEY"])
st.write("例:", st.secrets["SEARCH_ENDPOINT"])
st.write("例:", st.secrets["SEARCH_API_KEY"])
