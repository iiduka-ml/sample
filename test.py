# 
import streamlit as st
import os

from login import check_password

st.write('test')

system_msg = """
1. データの前処理とフィルタリング
まず、データの前処理を行い、必要な条件でデータをフィルタリングします。

python
コードをコピーする
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
for column in ['アクセル開度', 'エアコンON/OFF', 'エアコン設定温度', 'ブレーキスイッチON/OFF', '車両の速度', 'ODOメーターの値', '生涯IG-ON回数']:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# 欠損値の処理（例：行ごとに削除）
df.dropna(subset=['アクセル開度', 'エアコンON/OFF', 'エアコン設定温度', 'ブレーキスイッチON/OFF', '車両の速度', 'ODOメーターの値', '生涯IG-ON回数'], inplace=True)

# エアコンONの判定
df['エアコン使用中'] = df['エアコンON/OFF'].isin([1, 2, 4, 7]).astype(int)

# 条件に基づくデータのフィルタリング
df_filtered = df[(df['車両の速度'] <= 75) & (df['ODOメーターの値'] <= 120)]
2. 特徴量の作成
エアコンの使用時間を計算し、必要な特徴量を作成します。

python
コードをコピーする
# データを取得した時間をdatetime型に変換
df_filtered['データを取得した時間'] = pd.to_datetime(df_filtered['データを取得した時間'])

# エアコン使用時間の計算
df_filtered['エアコン使用時間'] = df_filtered['エアコン使用中'] * (df_filtered['データを取得した時間'].diff().dt.total_seconds().fillna(0))

# 車両ごとの累積エアコン使用時間を計算
df_filtered['累積エアコン使用時間'] = df_filtered.groupby('車両固有のID')['エアコン使用時間'].cumsum()

# 走行距離を計算
df_filtered['走行距離'] = df_filtered.groupby('車両固有のID')['ODOメーターの値'].diff().fillna(0)
df_filtered = df_filtered[df_filtered['走行距離'] > 0]  # 走行距離が正の値のみを使用
3. モデルの構築
特徴量を使ってバッテリーの予測モデルを構築します。

python
コードをコピーする
# 特徴量とターゲットの定義
features = df_filtered[['累積エアコン使用時間', '車両の速度', '走行距離']]
target = df_filtered['累積エアコン使用時間']  # 仮にバッテリー残量の代わりに使用

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
4. 結果の解釈
モデルの評価結果を確認し、予測精度を評価します。以下に主要なステップを日本語で説明します。

データの前処理: 不要なデータを削除し、数値に変換します。また、条件に基づきデータをフィルタリングします。
特徴量の作成: エアコンの使用時間を計算し、累積エアコン使用時間と走行距離を特徴量として定義します。
モデルの構築: 線形回帰モデルを使用して、バッテリーの予測モデルを構築します。
結果の解釈: モデルの評価指標を確認し、モデルの性能を評価します。
このプロセスを通じて、エアコンの使用時間、車速、走行距離からバッテリーの予測モデルを構築し、ユースケースに基づく仮説の検証を行います。
"""

st.write(system_msg)

