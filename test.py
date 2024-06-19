# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """

import pandas as pd

# サンプルデータを作成（実際のデータを読み込む場合は適宜変更してください）
data = {
    "アクセル開度": [0, 20, 30, 40],
    "エアコンON/OFF": [0, 1, 0, 1],
    "エアコン設定温度": [25, 30, 22, 15],
    "ブレーキスイッチON/OFF": [0, 1, 0, 1],
    "データを取得した時間": ["2024-06-01 12:00:00", "2024-06-01 13:00:00", "2024-06-01 14:00:00", "2024-06-01 15:00:00"],
    "車両固有のID": [1, 2, 3, 1],
    "ODOメーターの値": [1000, 1500, 2000, 2500],
    "生涯IG-ON回数": [10, 20, 30, 40],
    "車両の速度": [60, 70, 80, 90],
    "外気温": [10, 15, 20, 25]
}

df = pd.DataFrame(data)

# ①ユニークな「車両固有のID」の「エアコン利用者」および「エアコン不使用者」を定義
ac_users = df[(df["エアコン設定温度"] >= 0) & (df["エアコン設定温度"] <= 28)]["車両固有のID"].unique()
non_ac_users = df[(df["エアコン設定温度"] < 0) | (df["エアコン設定温度"] > 28)]["車両固有のID"].unique()

# ②「外気温」の値を1刻みにして、ユニークな「車両固有のID」の「エアコン利用者」および「エアコン不使用者」をカウント
result = []

for temp in range(51):  # 外気温は0から50まで
    ac_count = df[(df["外気温"] == temp) & (df["車両固有のID"].isin(ac_users))]["車両固有のID"].nunique()
    non_ac_count = df[(df["外気温"] == temp) & (df["車両固有のID"].isin(non_ac_users))]["車両固有のID"].nunique()
    result.append([temp, ac_count, non_ac_count])

result_df = pd.DataFrame(result, columns=["外気温", "エアコン利用者カウント", "エアコン不使用者"])

# ③結果をPrint
print(result_df)


"""

st.write(system_msg)

