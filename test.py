# 
import streamlit as st
import os

from login import check_password

st.write('test')

system_msg = """
import pandas as pd

# 仮のデータフレームを作成します（実際のデータで置き換えてください）
data = {
    'アクセル開度': [10, 20, 30, 40],
    'エアコンON/OFF': ['ON', 'OFF', 'ON', 'OFF'],
    'エアコン設定温度': [20, 25, 22, 21],
    'ブレーキスイッチON/OFF': ['ON', 'OFF', 'ON', 'OFF'],
    'データを取得した時間': ['2023-01-01 12:00', '2023-01-01 12:05', '2023-01-01 12:10', '2023-01-01 12:15'],
    '車両固有のID': [101, 102, 103, 104],
    'ODOメーターの値': [5000, 10000, 15000, 20000],
    '生涯IG-ON回数': [250, 260, 270, 280],
    '車両の速度': [110, 130, 125, 90]
}

df = pd.DataFrame(data)

# 条件1: 「車両の速度」が120以上のデータを抽出
df_speed_over_120 = df[df['車両の速度'] >= 120]

# 条件2: 「車両固有のID」のユニークなリストを取得
unique_ids = df_speed_over_120['車両固有のID'].unique()

# 条件3: ユニークな「車両固有のID」を用いてデータを再抽出
final_df = df[df['車両固有のID'].isin(unique_ids)]

# 結果を表示
print(final_df)
"""

st.write(system_msg)

