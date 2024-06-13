# 
import streamlit as st
import os

from login import check_password

st.write('test')

system_msg = """If the user is asked about a product, please include all information about each product.
                The user is an excellent salesman.
                Please advise according to the user's request.
                The user talks in a friendly tone, but somewhat difficult to understand.
                Be sure to conduct the conversation and evaluation in Japanese."""

st.write(system_msg)

