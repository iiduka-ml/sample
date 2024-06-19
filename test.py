# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """
import pandas as pd

# サンプルデータの作成（実際のデータを読み込む場合は適宜変更してください）
data = {
    "アクセル開度": [0, 10, 20, 30, 40],
    "エアコンON/OFF": [1, 0, 1, 1, 0],
    "エアコン設定温度": [25, 0, 18, 29, 30],
    "ブレーキスイッチON/OFF": [0, 1, 0, 0, 1],
    "データを取得した時間": ["2024-06-01 12:00:00", "2024-06-01 12:10:00", "2024-06-01 12:20:00", "2024-06-01 12:30:00", "2024-06-01 12:40:00"],
    "車両固有のID": [1, 2, 3, 1, 2],
    "ODOメーターの値": [10000, 15000, 20000, 25000, 30000],
    "生涯IG-ON回数": [100, 150, 200, 250, 300],
    "車両の速度": [50, 60, 70, 80, 90],
    "外気温": [25, 15, 35, 10, 50]
}

df = pd.DataFrame(data)

# ① ユニークな「車両固有のID」の「エアコン利用者」および「エアコン不使用者」を定義
df["エアコン利用者"] = df["エアコン設定温度"].apply(lambda x: "エアコン利用者" if 0 <= x <= 28 else "エアコン不使用者")

# ② 「外気温」の値を1刻みにして、ユニークな「車両固有のID」の「エアコン利用者」および「エアコン不使用者」をカウント
temperature_range = range(0, 51)
results = []

for temp in temperature_range:
    ac_users = df[(df["外気温"] == temp) & (df["エアコン利用者"] == "エアコン利用者")]["車両固有のID"].nunique()
    non_ac_users = df[(df["外気温"] == temp) & (df["エアコン利用者"] == "エアコン不使用者")]["車両固有のID"].nunique()
    results.append([temp, ac_users, non_ac_users])

# ③ 結果をPrint
print("「外気温」,「エアコン利用者カウント」,「エアコン不使用者カウント」")
for result in results:
    print(f"{result[0]},{result[1]},{result[2]}")

"""

st.write(system_msg)

