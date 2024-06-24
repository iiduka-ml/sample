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

# データフレームの定義とサンプルデータの挿入（調整済み）
df = pd.DataFrame({
    'accelerationpedal_position_004121': [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],
    'aircon_acstatus_font': [1, 2, 3, 4, 7, 1, 2, 3, 4, 7],
    'aircon_temperaturestting_dr': [20, 25, 30, 0, 15, 20, 25, 30, 0, 15],
    'brakesw': [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    'event_uniq_time': ['2024-06-24 10:00:00', '2024-06-24 10:05:00', '2024-06-24 10:10:00', '2024-06-24 10:15:00', '2024-06-24 10:20:00', 
                        '2024-06-24 10:25:00', '2024-06-24 10:30:00', '2024-06-24 10:35:00', '2024-06-24 10:40:00', '2024-06-24 10:45:00'],
    'hash_vin': ['VIN123', 'VIN123', 'VIN123', 'VIN123', 'VIN123', 'VIN124', 'VIN124', 'VIN124', 'VIN124', 'VIN124'],
    'odo_b500_km': [1000, 1010, 1020, 1030, 1040, 2000, 2010, 2020, 2030, 2040],
    'tsu_totaligcycle': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2],
    'vehiclespeed_meter_gw_004442': [60, 65, 70, 75, 80, 60, 65, 70, 75, 80],
    'outsidetemperatur_c': [25, 26, 27, 28, 29, 25, 26, 27, 28, 29]
})

# 数値に変換できない値をNaNに置換
df.replace('\\N', np.nan, inplace=True)

# すべての数値列を浮動小数点数に変換
for column in ['accelerationpedal_position_004121', 'aircon_acstatus_font', 'aircon_temperaturestting_dr', 'brakesw', 'vehiclespeed_meter_gw_004442', 'odo_b500_km', 'tsu_totaligcycle']:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# 欠損値の処理（例：行ごとに削除）
df.dropna(subset=['accelerationpedal_position_004121', 'aircon_acstatus_font', 'aircon_temperaturestting_dr', 'brakesw', 'vehiclespeed_meter_gw_004442', 'odo_b500_km', 'tsu_totaligcycle'], inplace=True)

# エアコンONの判定
df['エアコン使用中'] = df['aircon_acstatus_font'].apply(lambda x: 1 if x in [1, 2, 4, 7] else 0)

# データを取得した時間をdatetime型に変換
df['event_uniq_time'] = pd.to_datetime(df['event_uniq_time'])

# エアコン使用時間の計算
df['next_time'] = df.groupby('hash_vin')['event_uniq_time'].shift(-1)

def calculate_aircon_usage_time(row):
    if row['エアコン使用中'] == 1 and pd.notna(row['next_time']):
        usage_time = (row['next_time'] - row['event_uniq_time']).total_seconds() / 3600
        if usage_time < 0:
            return np.nan  # マイナスの値をNaNにする
        return usage_time
    return 0

df['エアコン使用時間'] = df.apply(calculate_aircon_usage_time, axis=1)

# 車両ごとの累積エアコン使用時間を計算
df['累積エアコン使用時間'] = df.groupby('hash_vin')['エアコン使用時間'].cumsum()

# 走行距離を計算
df['走行距離'] = df.groupby('hash_vin')['odo_b500_km'].diff().fillna(0)
df = df[df['走行距離'] > 0]  # 走行距離が正の値のみを使用

# エアコン利用者と不使用者の分類
ac_users = df[(df['aircon_temperaturestting_dr'] >= 0) & (df['aircon_temperaturestting_dr'] <= 28)]['hash_vin'].unique()
non_ac_users = df[(df['aircon_temperaturestting_dr'] < 0) | (df['aircon_temperaturestting_dr'] > 28)]['hash_vin'].unique()

# エアコン利用者と不使用者をデータフレームに追加
df['エアコン利用者'] = df['hash_vin'].apply(lambda x: 1 if x in ac_users else 0)
df['エアコン不使用者'] = df['hash_vin'].apply(lambda x: 1 if x in non_ac_users else 0)

# 条件に基づくデータのフィルタリング前のデータ数を表示
print(f'フィルタリング前のデータ数: {len(df)}')

# 条件に基づくデータのフィルタリング（緩和）
df_filtered = df[(df['vehiclespeed_meter_gw_004442'] <= 80) & (df['odo_b500_km'] >= 1000)]

# フィルタリング後のデータ数を表示
print(f'フィルタリング後のデータ数: {len(df_filtered)}')

# 特徴量とターゲットの定義
features = df_filtered[['累積エアコン使用時間', 'vehiclespeed_meter_gw_004442', '走行距離']]
target = df_filtered['累積エアコン使用時間']  # 仮にバッテリー消費の代わりに使用

# 特徴量とターゲットのデータ数を表示
print(f'特徴量データ数: {len(features)}')
print(f'ターゲットデータ数: {len(target)}')

# 訓練データとテストデータに分割
if len(features) > 0:
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

    # バッテリーの予測に関する出力
    print(f'累積エアコン使用時間が {np.mean(y_test):.2f} 時間でバッテリーがなくなります。')
else:
    print("フィルタリング後のデータがありません。条件を見直してください。")

フィルタリング前のデータ数: 8
フィルタリング後のデータ数: 8
特徴量データ数: 8
ターゲットデータ数: 8
平均二乗誤差 (MSE): 7.703719777548943e-34
決定係数 (R^2): 0.0
累積エアコン使用時間が 0.17 時間でバッテリーがなくなります。

"""

st.write(system_msg)

