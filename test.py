# 
import streamlit as st
import os

from login import check_password

st.write('　')


system_msg = """


import pandas as pd

# サンプルデータの作成（実際のデータを読み込む場合は、この部分を読み込むコードに置き換えてください）
data = {
    'アクセル開度': [10, 20, 30, 40, 50, 60],
    'エアコンON/OFF': [1, 0, 1, 0, 1, 1],
    'エアコン設定温度': [22, 23, 24, 25, 26, 22],
    'ブレーキスイッチON/OFF': [0, 1, 0, 1, 0, 1],
    'データを取得した時間': ['2024-01-01 10:00:00', '2024-01-01 11:00:00', '2024-01-02 10:00:00', '2024-01-02 11:00:00', '2024-01-03 10:00:00', '2024-01-03 11:00:00'],
    '車両固有のID': ['A', 'A', 'A', 'B', 'B', 'B'],
    'ODOメーターの値': [100, 150, 250, 200, 300, 350],
    '生涯IG-ON回数': [500, 501, 502, 500, 501, 502],
    '車両の速度': [60, 70, 80, 90, 100, 110],
    '外気温': [15, 16, 17, 18, 19, 20]
}

df = pd.DataFrame(data)
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

df_result_n_data = {
    '車両固有のID': ['A', 'B', 'C'],
    '100フラグ': [1, 0, 1]
}
df_result_n = pd.DataFrame(df_result_n_data)

# データの順序を確認
df = df.sort_values(by=['車両固有のID', 'データを取得した時間'])

# 次の時間をシフト
df['next_time'] = df.groupby('車両固有のID')['データを取得した時間'].shift(-1)

# 次の時間を確認
print(df[['車両固有のID', 'データを取得した時間', 'next_time']])

# エアコン使用時間の計算
def calculate_aircon_usage_time(row):
    if row['エアコンON/OFF'] == 1 and pd.notna(row['next_time']):
        return (row['next_time'] - row['データを取得した時間']).total_seconds() / 3600
    return 0

df['aircon_usage_time'] = df.apply(calculate_aircon_usage_time, axis=1)

# デバッグ: 計算結果を確認
print(df[['車両固有のID', 'データを取得した時間', 'next_time', 'エアコンON/OFF', 'aircon_usage_time']])

# エアコン使用時間の週単位集計
df['week'] = df['データを取得した時間'].dt.isocalendar().week
aircon_usage = df.groupby(['車両固有のID', 'week'])['aircon_usage_time'].sum().reset_index()

# 長距離運転ユーザーと非長距離運転ユーザーのエアコン使用時間
df_aircon_usage = pd.merge(aircon_usage, df_result_n, on='車両固有のID')

long_distance_users = df_aircon_usage[df_aircon_usage['100フラグ'] == 1].groupby('week')['aircon_usage_time'].mean().reset_index().rename(columns={'aircon_usage_time': '長距離運転ユーザー_エアコン使用時間'})
non_long_distance_users = df_aircon_usage[df_aircon_usage['100フラグ'] == 0].groupby('week')['aircon_usage_time'].mean().reset_index().rename(columns={'aircon_usage_time': '非長距離運転ユーザー_エアコン使用時間'})

# 結果を表示
result = pd.merge(long_distance_users, non_long_distance_users, on='week', how='outer').fillna(0)
import ace_tools as tools; tools.display_dataframe_to_user(name="Air Conditioner Usage per Week", dataframe=result)

result

"""

st.write(system_msg)

