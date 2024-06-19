# 
import streamlit as st
import os

from login import check_password

st.write('　')


system_msg = """

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import ttest_ind, linregress

# データの読み込み
df = pd.read_csv('your_vehicle_data.csv')

# データの前処理（例：データのクリーニング）
df = df.dropna()

# クラスタリングによる典型的なユースケースの特定
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[['アクセル開度', '車両の速度', '外気温', 'エアコン設定温度', 'ODOメーターの値']])
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)
cluster_counts = df['Cluster'].value_counts()
most_common_cluster = cluster_counts.idxmax()
print(f'最も一般的なクラスタ: {most_common_cluster}')
print(cluster_counts)

# 高速走行ユーザーの定義
speed_threshold = 80
user_speed_avg = df.groupby('車両固有のID')['車両の速度'].mean()
high_speed_users = user_speed_avg[user_speed_avg > speed_threshold].index

# エアコン使用時間の集計
ac_usage = df[df['エアコンON/OFF'] == 1]
ac_usage_time = ac_usage.groupby('車両固有のID').size()
ac_usage_high_speed = ac_usage_time[ac_usage_time.index.isin(high_speed_users)]
ac_usage_other = ac_usage_time[~ac_usage_time.index.isin(high_speed_users)]
mean_ac_usage_high_speed = ac_usage_high_speed.mean()
mean_ac_usage_other = ac_usage_other.mean()
print(f'高速走行ユーザーの平均エアコン使用時間: {mean_ac_usage_high_speed}')
print(f'その他のユーザーの平均エアコン使用時間: {mean_ac_usage_other}')
t_stat, p_value = ttest_ind(ac_usage_high_speed, ac_usage_other, equal_var=False)
print(f't検定の結果: t値 = {t_stat}, p値 = {p_value}')
if p_value < 0.05:
    print("統計的に有意な差があります。仮説が支持されます。")
else:
    print("統計的に有意な差はありません。仮説は支持されません。")

# バッテリーの低下要因の分析（回帰分析）
features = df[['アクセル開度', 'エアコンON/OFF', 'エアコン設定温度', '車両の速度']]
target = df['soc']
for feature in ['アクセル開度', 'エアコン設定温度', '車両の速度']:
    slope, intercept, r_value, p_value, std_err = linregress(features[feature], target)
    print(f'\n回帰分析の結果（{feature}とSoCの関係）:')
    print(f'傾き (slope): {slope}')
    print(f'切片 (intercept): {intercept}')
    print(f'決定係数 (R^2): {r_value**2}')
    print(f'p値: {p_value}')
    print(f'標準誤差 (std_err): {std_err}')
    if p_value < 0.05:
        print(f"{feature}とSoCの間には統計的に有意な関係があります。")
    else:
        print(f"{feature}とSoCの間には統計的に有意な関係はありません。")

# SoCの予測モデル
features = df[['アクセル開度', 'エアコンON/OFF', 'エアコン設定温度', '車両の速度', 'ODOメーターの値']]
target = df['soc']
scaled_features = scaler.fit_transform(features)
X_train, X_test, y_train, y_test = train_test_split(scaled_features, target, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'平均二乗誤差 (MSE): {mse}')
print(f'決定係数 (R^2): {r2}')
このコードにより、クラスタリングを使用して典型的なユースケースを特定し、SoC（バッテリー）の低下要因を分析し、さらにSoCの予測モデルを構築することができます。


"""

st.write(system_msg)

