# streamlit_app.py
import streamlit as st

st.write('test')
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
