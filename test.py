# 
import streamlit as st
import os

from login import check_password

st.write('test')

system_msg = """import pandas as pd

# ユニークな「車両固有のID」をもつデータの抽出
df_unique = df.drop_duplicates(subset='車両固有のID')

# 集計を行う
results = []
for vehicle_id in df_unique['車両固有のID']:
    # 各車両のデータを抽出
    vehicle_data = df[df['車両固有のID'] == vehicle_id]
    
    # 「車両の速度」のレコード数
    total_speed_records = len(vehicle_data)
    
    # 「車両の速度」が120キロ以上のレコード数
    count_speed_over_120 = (vehicle_data['車両の速度'] >= 120).sum()
    
    # 「120キロ以上の割合」の計算
    if total_speed_records > 0:
        percentage_over_120 = (count_speed_over_120 / total_speed_records) * 100
    else:
        percentage_over_120 = 0
    
    # 「120フラグ」の設定
    flag_120 = 1 if percentage_over_120 >= 40 else 0
    
    # 結果の保存
    results.append({
        'ユニーク車両固有のID': vehicle_id,
        '120キロ以上の割合': percentage_over_120,
        '120フラグ': flag_120
    })

# 結果のデータフレーム化
results_df = pd.DataFrame(results)

# 結果の表示
print(results_df)"""

st.write(system_msg)

