# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """

df = pd.DataFrame(data)

# エアコン利用者と不使用者を識別する
ac_users = df[df['エアコン設定温度'].between(0, 28)]['車両固有のID'].unique()
non_ac_users = df[~df['エアコン設定温度'].between(0, 28)]['車両固有のID'].unique()

# エアコン利用者、不使用者をラベル付けする
df['エアコン利用者'] = df['車両固有のID'].apply(lambda x: 'エアコン利用者' if x in ac_users else 'エアコン不使用者')

# 外気温でグループ化し、エアコン利用者、不使用者のカウントを行う
result = df.groupby(['外気温', 'エアコン利用者'])['車両固有のID'].nunique().unstack(fill_value=0).reset_index()

# 列名を日本語に変更
result.columns = ['外気温', 'エアコン不使用者カウント', 'エアコン利用者カウント']

# 結果を表示
print(result)


"""

st.write(system_msg)

