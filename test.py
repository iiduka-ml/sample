# 
import streamlit as st
import os

from login import check_password

st.write('test')

system_msg = """

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# データの読み込み
df = pd.read_csv('your_vehicle_data.csv')

# 数値に変換できない値をNaNに置換
df.replace('\\N', np.nan, inplace=True)

# すべての数値列を浮動小数点数に変換
for column in ['accelerationpedal_position_004121', 'aircon_acstatus_font', 'aircon_temperaturestting_dr', 'brakesw', 'vehiclespeed_meter_gw_004442', 'odo_b500_km', 'tsu_totaligcycle']:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# 欠損値の処理（例：行ごとに削除）
df.dropna(subset=['accelerationpedal_position_004121', 'aircon_acstatus_font', 'aircon_temperaturestting_dr', 'brakesw', 'vehiclespeed_meter_gw_004442', 'odo_b500_km', 'tsu_totaligcycle'], inplace=True)

# エアコンONの判定
df['エアコン使用中'] = df['aircon_acstatus_font'].apply(lambda x: 1 if x == 'ON' else 0)

# 条件に基づくデータのフィルタリング
df_filtered = df[(df['vehiclespeed_meter_gw_004442'] <= 75) & (df['odo_b500_km'] <= 120)]

# データを取得した時間をdatetime型に変換
df_filtered['event_uniq_time'] = pd.to_datetime(df_filtered['event_uniq_time'])

# エアコン使用時間の計算
df_filtered['エアコン使用時間'] = df_filtered['エアコン使用中'] * (df_filtered['event_uniq_time'].diff().dt.total_seconds().fillna(0))

# 車両ごとの累積エアコン使用時間を計算
df_filtered['累積エアコン使用時間'] = df_filtered.groupby('hash_vin')['エアコン使用時間'].cumsum()

# 走行距離を計算
df_filtered['走行距離'] = df_filtered.groupby('hash_vin')['odo_b500_km'].diff().fillna(0)
df_filtered = df_filtered[df_filtered['走行距離'] > 0]  # 走行距離が正の値のみを使用

# 特徴量とターゲットの定義
features = df_filtered[['累積エアコン使用時間', 'vehiclespeed_meter_gw_004442', '走行距離']]
target = df_filtered['累積エアコン使用時間']  # 仮にバッテリー消費の代わりに使用

# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 線形回帰モデルの構築
model = LinearRegression()

# モデルの訓練
model.fit(X_train, y_train)

# 予測の実施
y_pred = model.predict(X_test)

# モデルの評価
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'平均二乗誤差 (MSE): {mse}')
print(f'決定係数 (R^2): {r2}')

"""

st.write(system_msg)

