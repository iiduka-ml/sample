# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """
# 各グループに対して、高速道路での利用時間を計算し、全体の40％以上かどうか判断
def calculate_highway_usage_time(group):
    # 全体の時間を計算
    total_duration = (group['データを取得した時間'].max() - group['データを取得した時間'].min()).total_seconds()
    
    # 速度が120km/h以上のデータ点を抽出し、時間差を計算
    high_speed_data = group[group['車両の速度'] >= 120]
    high_speed_data['時間差'] = high_speed_data['データを取得した時間'].diff().dt.total_seconds()
    high_speed_data['時間差'].fillna(0, inplace=True)
    high_speed_usage_time = high_speed_data['時間差'].sum()
    
    # 高速道路利用時間が全体の40%以上かどうか判断
    if high_speed_usage_time >= 0.4 * total_duration:
        return high_speed_usage_time
    else:
        return 0  # 40%未満の場合は0を返す（高速道路としてカウントしない）

# 各走行の高速道路利用時間を計算
highway_usage_time = grouped.apply(calculate_highway_usage_time)

# 結果の表示
print(highway_usage_time)
"""

st.write(system_msg)

