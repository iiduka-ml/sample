# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """
import pandas as pd

# 仮のデータフレームを作成します（実際のデータで置き換えてください）
data = {
    'アクセル開度': [10, 20, 30, 40, 50],
    'エアコンON/OFF': ['ON', 'OFF', 'ON', 'OFF', 'ON'],
    'エアコン設定温度': [20, 25, 22, 21, 23],
    'ブレーキスイッチON/OFF': ['ON', 'OFF', 'ON', 'OFF', 'ON'],
    'データを取得した時間': ['2023-01-01 12:00', '2023-01-01 12:05', '2023-01-01 12:10', '2023-01-01 12:15', '2023-01-01 12:20'],
    '車両固有のID': [101, 101, 102, 102, 102],
    'ODOメーターの値': [5000, 5500, 6000, 6500, 7000],
    '生涯IG-ON回数': [250, 251, 260, 261, 262],
    '車両の速度': [110, 115, 120, 125, 130]
}

df = pd.DataFrame(data)

# データを「車両固有のID」でグループ化し、「生涯IG-ON回数」と「ODOメーターの値」に対して処理を行う
grouped = df.groupby('車両固有のID').agg({
    '生涯IG-ON回数': 'max',  # 最大の「生涯IG-ON回数」を取得
    'ODOメーターの値': lambda x: x.max() - x.min()  # 「ODOメーターの値」の最大値と最小値の差を計算
}).reset_index()  # インデックスをリセットして「車両固有のID」をカラムに戻す

# 新しいデータフレーム名を 'cumulative_trips' に設定
cumulative_trips = grouped.rename(columns={
    '生涯IG-ON回数': '最大生涯IG-ON回数',
    'ODOメーターの値': 'ODOメーター差'
})

# 結果を表示
print(cumulative_trips)
"""

st.write(system_msg)

