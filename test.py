# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """

import pandas as pd

# データの読み込み（ファイルパスは適宜調整してください）
df = pd.read_csv('path_to_your_data.csv')

# 「データを取得した時間」をdatetime型に変換
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

# 各「車両固有のID」と「生涯IG-ON回数」の組み合わせごとにグループ化し、各走行でのデータを集約
grouped = df.groupby(['車両固有のID', '生涯IG-ON回数'])

# 高速道路利用判定と最小時間の記録
def highway_usage(group):
    min_time = group['データを取得した時間'].min()
    total_duration = (group['データを取得した時間'].max() - min_time).total_seconds()
    high_speed_duration = group[group['車両の速度'] >= 120]['データを取得した時間'].diff().dt.total_seconds().sum()
    highway_usage = 1 if high_speed_duration / total_duration > 0.4 else 0
    return pd.Series({'Highway Usage': highway_usage, 'Min Time': min_time})

# 各走行の高速道路利用有無と最小時間
highway_uses = grouped.apply(highway_usage)

# 週間平均の高速道路利用回数を計算
weekly_average_usage = highway_uses.groupby('車両固有のID').resample('W', on='Min Time').sum().groupby('車両固有のID').mean()

# 結果の表示
print(weekly_average_usage)
"""

st.write(system_msg)

