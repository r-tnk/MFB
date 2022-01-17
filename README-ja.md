[English README is here](https://github.com/r-tnk/MFB/blob/main/README.md)

# MFB (ModEM File Builder)

## 概要
比抵抗構造インバージョンコード　ModEM (Egbert and Kelbert, 2012)の前処理と後処理を簡単に行えるGUIソフトウェアです。

![SS1](https://user-images.githubusercontent.com/62272721/149767139-ca5f9ed0-e652-457a-850f-d86f37ece25d.png)

![SS2](https://user-images.githubusercontent.com/62272721/149767262-2c74b5d9-d618-4099-ac5d-05501586095d.png)

## 特徴

- シンプルなGUI
- 前処理と後処理を一つのソフトウェアで実行可能
- 地形を考慮した初期比抵抗構造の作成
- 作成したグリッドと観測点の自動描画
- 観測値と計算値（見かけ比抵抗と位相）を簡単に比較
- 比抵抗構造・震源・その他の点（観測点や地盤変動源など）を簡単にparaview形式のファイルに書き出し
- 感度検定のために簡単に比抵抗構造の一部改変が可能

## 必要なもの

- python3 以上
- pandas
- numpy
- matplotlib
- seaborn
- pyevtk
- pyproj
- PysimpleGUI

## 使い方
1. DEMと海底地形データ（必要であれば）を用意
2. 観測点の緯度経度が書かれたファイルを用意
3. 変換先の直交座標系のEPSGコードを調査(https://epsg.io/)
4. MFBを起動

    `$ python mfb_gui.py`

5. GUI上で設定値を更新（Save Settingsボタンを押す）
6. ファイルを作成（Make Filesボタンを押す）
7. ModEMでインバージョン
8. MFBで後処理

## インストール

gitからのインストールはインストールしたいディレクトリで以下のコマンドを実行。

    $ git clone https://github.com/r-tnk/MFB.git

## 開発者

[R. Tanaka](https://www.researchgate.net/profile/Ryo-Tanaka-12)

## 著作権

[MIT](https://github.com/r-tnk/MFB/blob/main/LICENSE)