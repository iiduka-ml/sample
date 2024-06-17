# 
import streamlit as st
import os

from login import check_password

st.write('　')

system_msg = """
pip install jupyterlab "ipywidgets>=7.6"

26からはじまるデータを利用


5.
現在、FireboxでJupyterLabでNotebookを使ってます
相談なんだけど、今dfに「アクセル開度」、「エアコンON/OFF」、「エアコン設定温度」、「ブレーキスイッチON/OFF」、「データを取得した時間」、「車両固有のID」、「ODOメーターの値」、「生涯IG-ON回数」、「車両の速度」　の車両データがはいってます。以下条件で作成して。日本語でお願いします。
※「データを取得した時間」のデータ→YYYY-MM-DD HH:mm
※「生涯IG-ON回数」は1回の乗車のカウントになります
・ユニークな「車両固有のID」(つまりユニークなユーザー)の1週間の平均乗車日数を求めたい
（「データを取得した時間」カラムを日付型に変換し、それを元に「車両固有のID」ごとにグループ化し、各グループについて1週間ごとの乗車日数を計算）
・グループ化する時に「生涯IG-ON回数」も集計にいれてください

ありがとう　最後に、「車両の速度」が120以上を抽出し、「車両の速度」が120以上の平均乗車日数を算出してください。　print(average_rides_per_week)　の下に制御を記述してください。　日本語でお願いします。
＜コード＞



「データを取得した時間」カラムを日付型に変換し、それを元に「車両固有のID」ごとにグループ化し、各グループについて1週間ごとの乗車日数を計算

次に120km/h以上の速度で走行している記録を抽出し、それらのデータに対して「週番号」を計算し直します。その後、抽出されたデータに対して同様に週ごとの乗車日数を集計し、車両固有のIDごとにその平均を求めています。最終的には、全体の平均乗車日数と高速走行時の平均乗車日数を別々に表示

import pandas as pd

# データフレームの例です（dfという名前で読み込まれていると仮定）
# df = pd.read_csv('file_path.csv')  # CSVファイルから読み込む場合

# 「データを取得した時間」カラムを日付型に変換
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

# '車両固有のID' と 'データを取得した時間'（日付のみ）でグループ化し、'生涯IG-ON回数' を集計
df['取得日'] = df['データを取得した時間'].dt.date  # 時間を除外して日付のみにする
weekly_rides = df.groupby(['車両固有のID', pd.Grouper(key='データを取得した時間', freq='W')])['生涯IG-ON回数'].nunique()

# 各車両固有のIDごとに週平均乗車日数を計算
average_weekly_rides = weekly_rides.groupby('車両固有のID').mean().reset_index()

# 結果を表示
print(average_weekly_rides)

＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

# '車両の速度' が120以上のデータを抽出
high_speed_df = df[df['車両の速度'] >= 120]

# 高速走行のデータに対して週番号を計算
high_speed_df['週番号'] = high_speed_df['データを取得した時間'].dt.isocalendar().week

# 高速走行のデータに基づいて、車両固有のIDごとに1週間ごとの乗車日数を計算
high_speed_weekly_rides = high_speed_df.groupby(['車両固有のID', '週番号']).agg({'データを取得した時間': 'nunique'}).reset_index()

# 高速走行における各車両固有のIDごとに平均乗車日数を計算
high_speed_average_rides_per_week = high_speed_weekly_rides.groupby('車両固有のID')['データを取得した時間'].mean().reset_index()
high_speed_average_rides_per_week.rename(columns={'データを取得した時間': '平均乗車日数'}, inplace=True)

# 結果を表示
print("全体の平均乗車日数:")
print(average_rides_per_week)
print("\n速度120km/h以上の平均乗車日数:")
print(high_speed_average_rides_per_week)

or

# 「車両の速度」が120以上のデータを抽出
high_speed_df = df[df['車両の速度'] >= 120]

# 高速で走行している日付でグループ化し、「生涯IG-ON回数」を集計
high_speed_df['取得日'] = high_speed_df['データを取得した時間'].dt.date  # 時間を除外して日付のみにする
high_speed_weekly_rides = high_speed_df.groupby(['車両固有のID', pd.Grouper(key='データを取得した時間', freq='W')])['生涯IG-ON回数'].nunique()

# 各車両固有のIDごとに高速での週平均乗車日数を計算
average_high_speed_weekly_rides = high_speed_weekly_rides.groupby('車両固有のID').mean().reset_index()

# 平均乗車日数を表示
print(average_high_speed_weekly_rides)

6.

現在、FireboxでJupyterLabでNotebookを使ってます
相談なんだけど、今dfに「アクセル開度」、「エアコンON/OFF」、「エアコン設定温度」、「ブレーキスイッチON/OFF」、「データを取得した時間」、「車両固有のID」、「ODOメーターの値」、「生涯IG-ON回数」、「車両の速度」　の車両データがはいってます。以下条件でコードを作成して。日本語でお願いします。

＜条件＞
※「データを取得した時間」のデータ→YYYY-MM-DD HH
※「生涯IG-ON回数」は1回の乗車のカウントになります
①「車両の速度」が120以上を抽出してください
②①の結果にて、ユニークな「車両固有のID」(つまりユニークなユーザー)の1週間の平均走行距離を算出してください。※「ODOメーターの値」に走行距離の累計(km)がはいってます　つまり、「車両固有のID」の1週間の走行距離は「データを取得した時間」で週を、「ODOメーターの値」でその週のMax値からMin値を引けば走行距離が出ます。複数の週が算出された場合は、その平均値としてください
③グループ化する時に「生涯IG-ON回数」も集計にいれてください


このコードは以下のステップを実行します：

サンプルデータをDataFrameとして設定します。
「データを取得した時間」カラムを日付型に変換します。
「車両の速度」が120km/h以上のデータをフィルタリングします。
新たに「週番号」カラムを追加し、日付データから週番号を計算します。
「車両固有のID」と「週番号」ごとにグループ化し、各週の走行距離（最大値 - 最小値）を計算します。
最後に、各車両固有のIDごとに平均走行距離を算出し、表示します。
注意点として、df_high_speed['週番号'] = df_high_speed['データを取得した時間'].dt.isocalendar().week はデータフレームのコピーに直接変更を加えるため、SettingWithCopyWarningが出る可能性があります。実際の環境で問題が発生する場合は、.copy()を使用するか、元のデータフレームから直接変更する方法を検討してください。

まずは「車両の速度」が120km/h以上のデータを抽出し、その後、それぞれのユニークな「車両固有のID」ごとに1週間の平均走行距離を算出する

import pandas as pd

# dfはあなたのデータフレームの名前と仮定します
# 'データを取得した時間' を datetime 型に変換して、必要な形式にフォーマット
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間']).dt.strftime('%Y-%m-%d %H')

# ①「車両の速度」が120以上のデータを抽出
df_speed_over_120 = df[df['車両の速度'] >= 120]

# ② ユニークな「車両固有のID」の1週間の平均走行距離を算出
# 「データを取得した時間」の週を算出し、その週ごとに「ODOメーターの値」の最大値と最小値を計算
df_speed_over_120['週'] = pd.to_datetime(df_speed_over_120['データを取得した時間']).dt.to_period('W').dt.start_time
weekly_distance = df_speed_over_120.groupby(['車両固有のID', '週']).agg(
    最大ODO=('ODOメーターの値', 'max'),
    最小ODO=('ODOメーターの値', 'min'),
    生涯IG_ON回数=('生涯IG-ON回数', 'max')  # 生涯IG-ON回数も集計に入れる
)
weekly_distance['週間走行距離'] = weekly_distance['最大ODO'] - weekly_distance['最小ODO']

# 「車両固有のID」ごとに平均走行距離を算出
average_weekly_distance = weekly_distance.groupby('車両固有のID')['週間走行距離'].mean()

# 結果を表示
print(average_weekly_distance)
print(weekly_distance.reset_index())

ありがとう　最後に、「週間走行距離」が500以上の割合を％で算出してください。　printprint(weekly_distance.reset_index())の下に制御を記述してください。　日本語でお願いします。
＜コード＞
# 「週間走行距離」が500km以上の割合を計算
over_500_km_ratio = (weekly_distance['週間走行距離'] >= 500).mean() * 100
print(f"週間走行距離が500km以上の割合: {over_500_km_ratio:.2f}%")


7.

1DC(IG-ONからIG-OFF）までの時間のうち、40％以上の時間を　120km/hで走行　を高速利用とする

「車両の速度」が120以上のデータを抽出
①ユニークな「車両固有のID」および「生涯IG-ON回数」のグループ化をします
②

※「生涯IG-ON回数」には数字がはいっていて、例えばユニークな「車両固有のID」に対して、「生涯IG-ON回数」の値が500,501,502と3つの数字がはいっていたとしたら、そのユニークな「車両固有のID」は、「データを取得した時間」で指定した期間で、3回の走行実績がある事になります

※1.を参照の事
※1の結果に高速道路のユーザーに「道路種別」フラグを立てる

現在、FireboxでJupyterLabでNotebookを使ってます
相談なんだけど、今dfに「アクセル開度」、「エアコンON/OFF」、「エアコン設定温度」、「ブレーキスイッチON/OFF」、「データを取得した時間」、「車両固有のID」、「ODOメーターの値」、「生涯IG-ON回数」、「車両の速度」「道路種別」　の車両データがはいってます。以下条件でコードを作成して。日本語でお願いします。
※「データを取得した時間」のデータ→YYYY-MM-DD HH:mm:ss
※「道路種別」には1若しくは0の値がはいっており、1の場合は高速道路利用した車両の位置づけになります
①「車両の速度」が120以上のデータを抽出
②ユニークな「車両固有のID」(つまりユニークなユーザー)の1週間の高速道路平均利用回数を求めたい

# ① 車両の速度が120km/h以上のデータを抽出
df_high_speed = df[df['車両の速度'] >= 120]

# ② ユニークな「車両固有のID」の1週間の高速道路平均利用回数を求める
# 「データを取得した時間」をdatetime型に変換
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])

# 週ごとにデータをグループ化し、高速道路利用の平均回数を計算
weekly_highway_usage = df[df['道路種別'] == 1].groupby([pd.Grouper(key='データを取得した時間', freq='W'), '車両固有のID']).size()
weekly_highway_average = weekly_highway_usage.groupby('車両固有のID').mean()

# 結果を表示
print("車両の速度が120km/h以上のデータ:")
print(df_high_speed)
print("\nユニークな車両固有のIDごとの1週間の高速道路平均利用回数:")
print(weekly_highway_average)

8.
前提条件として、高速走行ユーザーでいいですか？
★長距離と長い時間の質問
今車両の分析をしているのですが、1回の運転で、長距離　および　長時間の運転時間　の定義ってどれくらいかな？　アドバイスください

長距離運転:一度の運転で100キロメートル以上
長時間運転:連続して2時間以上運転

現在、FireboxでJupyterLabでNotebookを使ってます
相談なんだけど、今dfに「アクセル開度」、「エアコンON/OFF」、「エアコン設定温度」、「ブレーキスイッチON/OFF」、「データを取得した時間」、「車両固有のID」、「ODOメーターの値」、「生涯IG-ON回数」、「車両の速度」　の車両データがはいってます。以下条件でコードを作成して。日本語でお願いします。

・長距離運転のユーザー(ユニークな「車両固有のID」)の週当たりのエアコン使用時間
・長距離運転しないユーザー(ユニークな「車両固有のID」)の週当たりのエアコン使用時間
※「データを取得した時間」のデータ→YYYY-MM-DD HH:mm:ss
※「ODOメーターの値」は「生涯IG-ON回数」の数字をキーに「ODOメーターの値」の最大値から最小値を引いた値が、「車両固有のID」が1回の走行距離になります
※「生涯IG-ON回数」には数字がはいっていて、例えばユニークな「車両固有のID」に対して、「生涯IG-ON回数」の値が500,501,502と3つの数字がはいっていたとしたら、そのユニークな「車両固有のID」は、「データを取得した時間」で指定した期間で、3回の走行実績がある事になります
※長距離運転は1回の運転(1回の走行距離)が100以上になります

import pandas as pd

# データを読み込み、適切な型に変換
df['データを取得した時間'] = pd.to_datetime(df['データを取得した時間'])
df['エアコンON/OFF'] = df['エアコンON/OFF'].apply(lambda x: 1 if x == 'ON' else 0)

# 車両ごと、生涯IG-ON回数ごとに最大ODOと最小ODOを計算
odo_stats = df.groupby(['車両固有のID', '生涯IG-ON回数']).agg(
    最小ODO=('ODOメーターの値', 'min'),
    最大ODO=('ODOメーターの値', 'max'),
    最初の時間=('データを取得した時間', 'min'),
    最後の時間=('データを取得した時間', 'max'),
    エアコン使用時間=('エアコンON/OFF', 'sum')  # エアコンがONになっている総時間
)

# 走行距離を計算
odo_stats['走行距離'] = odo_stats['最大ODO'] - odo_stats['最小ODO']

# 長距離運転を定義（1回の走行距離が100km以上）
odo_stats['長距離運転'] = odo_stats['走行距離'] >= 100

# エアコン使用時間を時間単位で算出（サンプルデータの頻度による）
odo_stats['エアコン使用時間'] = odo_stats['エアコン使用時間'] * (odo_stats['最後の時間'] - odo_stats['最初の時間']).dt.total_seconds() / 3600

# 週ごとにデータをまとめる
odo_stats['週'] = odo_stats['最初の時間'].dt.to_period('W').dt.start_time
weekly_ac_usage = odo_stats.groupby(['車両固有のID', '週', '長距離運転'])['エアコン使用時間'].sum().reset_index()

# 長距離運転と非長距離運転の平均エアコン使用時間を出力
long_distance_ac = weekly_ac_usage[weekly_ac_usage['長距離運転'] == True].groupby('車両固有のID')['エアコン使用時間'].mean()
short_distance_ac = weekly_ac_usage[weekly_ac_usage['長距離運転'] == False].groupby('車両固有のID')['エアコン使用時間'].mean()

print("長距離運転ユーザーの週当たり平均エアコン使用時間:")
print(long_distance_ac)
print("非長距離運転ユーザーの週当たり平均エアコン使用時間:")
print(short_distance_ac)

データの準備: 'データを取得した時間' を datetime 型に変換し、'エアコンON/OFF' を数値に変換します。
集計: 各 '車両固有のID' と '生涯IG-ON回数' ごとに ODOメーターの値の最大・最小を計算し、走行距離を導出します。
長距離運転の判定: 一回の走行距離が100km以上の場合を長距離と定義します。
エアコン使用時間の計算: ONになっている時間の総和を時間単位で計算します。
週ごとの集計: 各週ごとにデータをまとめ、長距離と非長距離のユーザーごとにエアコン使用時間を集計します。

9.
★
前提条件として、高速走行ユーザーでいいですか？
外気温のカラムは何になりますでしょうか？

現在、FireboxでJupyterLabでNotebookを使ってます
相談なんだけど、今dfに「アクセル開度」、「エアコンON/OFF」、「エアコン設定温度」、「ブレーキスイッチON/OFF」、「データを取得した時間」、「車両固有のID」、「ODOメーターの値」、「生涯IG-ON回数」、「車両の速度」「外気温」　の車両データがはいってます。以下条件でコードを作成して。日本語でお願いします。

・「車両固有のID」、「エアコンON/OFF」、「エアコン設定温度」、「外気温」で集計して
・外気温が何度の時、エアコンをつけるのか　1度刻みで「車両固有のID」をカウントしてください
"""

st.write(system_msg)

