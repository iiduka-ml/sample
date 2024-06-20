# 
import streamlit as st
import os

from login import check_password

st.write('　')


system_msg = """

df = pd.DataFrame(data)
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

df_result_n_data = {
    '車両固有のID': ['A', 'B', 'C'],
    '100フラグ': [1, 0, 1]
}
df_result_n = pd.DataFrame(df_result_n_data)

# エアコンON/OFFを数値型に変換
df['エアコンON/OFF'] = df['エアコンON/OFF'].replace('\\N', np.nan).astype(float).fillna(0).astype(int)

# データの順序を確認
df = df.sort_values(by=['車両固有のID', 'データを取得した時間'])

# 次の時間をシフト
df['next_time'] = df.groupby('車両固有のID')['データを取得した時間'].shift(-1)

# エアコン使用時間の計算
def calculate_aircon_usage_time(row):
    if row['エアコンON/OFF'] in [1, 2, 4, 7] and pd.notna(row['next_time']):
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

