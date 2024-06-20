# 
import streamlit as st
import os

from login import check_password

st.write('　')


system_msg = """

df = pd.DataFrame(data)
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

# テスト用のIDを指定
test_id = 'A'

# 特定のIDのデータを抽出
df_test = df[df['車両固有のID'] == test_id].copy()

# データの順序を確認
df_test = df_test.sort_values(by=['データを取得した時間'])

# 次の時間をシフト
df_test['next_time'] = df_test['データを取得した時間'].shift(-1)

# エアコン使用時間の計算
df_test['aircon_usage_time'] = df_test.apply(lambda row: (row['next_time'] - row['データを取得した時間']).total_seconds() / 3600 if row['エアコンON/OFF'] == 1 and pd.notna(row['next_time']) else 0, axis=1)

# 結果を表示
print(df_test[['車両固有のID', 'データを取得した時間', 'next_time', 'エアコンON/OFF', 'aircon_usage_time']])


result

"""

st.write(system_msg)

