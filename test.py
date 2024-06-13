# 
import streamlit as st
import os

from login import check_password

st.write('test')

system_msg = """
# フラグが1のレコード数
flag_1_count = results_df['120フラグ'].sum()

# 全レコード数
total_records = len(results_df)

# フラグが1の割合の計算
flag_1_ratio = (flag_1_count / total_records) * 100

print(f"「120フラグ」が1の割合: {flag_1_ratio:.2f}%")
"""

st.write(system_msg)

