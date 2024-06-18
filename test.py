# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """

特定の「車両固有のID」ごとに1週間の平均高速道路利用回数を計算するPythonのコードを作成します。以下は、そのために必要な手順を含むコードの例です。

まずは、データを適切に処理して分析を行うためのステップを設定しましょう。

データの準備: Pandasライブラリを使用してデータを読み込み、適切に整形します。
走行実績の抽出: 各「車両固有のID」について、「生涯IG-ON回数」を基に走行実績を算出します。
高速道路利用の判定: 各走行実績ごとに、高速道路での利用時間が40%以上かどうかを判断します。
週間平均の計算: 各「車両固有のID」ごとに週間の平均高速道路利用回数を計算します。

import pandas as pd

# データの読み込み（ファイルパスは適宜調整してください）
df = pd.read_csv('path_to_your_data.csv')

# 「データを取得した時間」をdatetime型に変換
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

# 各「車両固有のID」と「生涯IG-ON回数」の組み合わせごとにグループ化し、各走行でのデータを集約
grouped = df.groupby(['車両固有のID', '生涯IG-ON回数'])

# 高速道路利用判定
def highway_usage(group):
    total_duration = (group['データを取得した時間'].max() - group['データを取得した時間'].min()).total_seconds()
    high_speed_duration = group[group['車両の速度'] >= 120]['データを取得した時間'].diff().dt.total_seconds().sum()
    if high_speed_duration / total_duration > 0.4:
        return 1
    return 0

# 各走行の高速道路利用有無
highway_uses = grouped.apply(highway_usage)

# 週間平均の高速道路利用回数を計算
weekly_average_usage = highway_uses.groupby('車両固有のID').resample('W', on='データを取得した時間').sum().groupby('車両固有のID').mean()

# 結果の表示
print(weekly_average_usage)
"""

st.write(system_msg)

