# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """

# ② 「外気温」の値を1刻みにして、ユニークな「車両固有のID」の「エアコン利用者」および「エアコン不使用者」をカウント
temperature_range = range(0, 51)

# 結果を保存するためのデータフレームを作成
results_df = pd.DataFrame(temperature_range, columns=["外気温"])
results_df["エアコン利用者カウント"] = 0
results_df["エアコン不使用者カウント"] = 0

for temp in temperature_range:
    ac_users = df[(df["外気温"] == temp) & (df["エアコン利用者"] == "エアコン利用者")]["車両固有のID"].nunique()
    non_ac_users = df[(df["外気温"] == temp) & (df["エアコン利用者"] == "エアコン不使用者")]["車両固有のID"].nunique()
    results_df.loc[results_df["外気温"] == temp, "エアコン利用者カウント"] = ac_users
    results_df.loc[results_df["外気温"] == temp, "エアコン不使用者カウント"] = non_ac_users

# ③ 結果をPrint
print("「外気温」,「エアコン利用者カウント」,「エアコン不使用者カウント」")
for index, row in results_df.iterrows():
    print(f"{row['外気温']},{row['エアコン利用者カウント']},{row['エアコン不使用者カウント']}")

"""

st.write(system_msg)

