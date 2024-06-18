# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """
import pandas as pd

# データの読み込み（適切なファイルパスを設定してください）
df = pd.read_csv('path_to_your_data.csv')

# 「データを取得した時間」の列を datetime 型に変換
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

# 「車両固有のID」と「生涯IG-ON回数」でグループ化
grouped = df.groupby(['車両固有のID', '生涯IG-ON回数'])

# 各グループに対して、高速道路での利用時間を計算
def calculate_highway_usage_time(group):
    # 速度が120km/h以上のデータ点を抽出
    high_speed_data = group[group['車両の速度'] >= 120]
    
    # 時間差を計算（隣接するデータポイント間）
    high_speed_data['時間差'] = high_speed_data['データを取得した時間'].diff().dt.total_seconds()
    
    # 最初のデータポイントの時間差は計算できないため、0とする
    high_speed_data['時間差'].fillna(0, inplace=True)
    
    # 高速道路の利用時間の合計を返す
    return high_speed_data['時間差'].sum()

# 各走行の高速道路利用時間を計算
highway_usage_time = grouped.apply(calculate_highway_usage_time)

# 結果の表示
print(highway_usage_time)
"""

st.write(system_msg)

