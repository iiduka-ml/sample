# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """

df = pd.DataFrame(data)

# データを取得した時間をdatetime型に変換
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

# 「車両固有のID」と「生涯IG-ON回数」でグループ化
grouped = df.groupby(['車両固有のID', '生涯IG-ON回数'])

# 1回の走行距離（ODOメーターの値のMAX値からMIN値を引いたもの）を計算
df_result = grouped['ODOメーターの値'].agg(['max', 'min'])
df_result['走行距離'] = df_result['max'] - df_result['min']

# 100フラグを設定
df_result['100フラグ'] = df_result['走行距離'] >= 100

# 必要な列を選択して新しいデータフレームを作成
df_result = df_result.reset_index()
df_result = df_result[['車両固有のID', '生涯IG-ON回数', '走行距離', '100フラグ']]

# 結果を表示
import ace_tools as tools; tools.display_dataframe_to_user(name="Long Distance Driving Data", dataframe=df_result)

df_result
このコードでは、以下のステップを実行しています：

サンプルデータの作成（実際のデータを読み込む場合は適宜修正）。
「データを取得した時間」をdatetime型に変換。
「車両固有のID」と「生涯IG-ON回数」でグループ化。
グループ化されたデータに対して、「ODOメーターの値」の最大値と最小値を取得し、それらの差から走行距離を計算。
走行距離が100km以上かどうかのフラグを設定。
必要な列（「車両固有のID」、「生涯IG-ON回数」、「走行距離」、「100フラグ」）を選択して新しいデータフレームを作成。
"""

st.write(system_msg)

