# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """
import pandas as pd

# 「データを取得した時間」を日付型に変換
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

# フラグが1の車両固有のIDを取得
flagged_vehicle_ids = results_df[results_df['120フラグ'] == 1]['ユニーク車両固有のID']

# フラグが1の車両のデータを抽出
flagged_data = df[df['車両固有のID'].isin(flagged_vehicle_ids)]

# 1週間ごとに「車両の速度」が120キロ以上のレコードをカウント
weekly_counts = flagged_data[flagged_data['車両の速度'] >= 120].groupby(['車両固有のID', pd.Grouper(key='データを取得した時間', freq='W')]).size()

print(weekly_counts)

"""

st.write(system_msg)

