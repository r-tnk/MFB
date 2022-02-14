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
1. DEM(headerに[lon lat height]が必要）と海底地形データ（必要であれば。headerに[lon lat depth]が必要）を用意
2. 観測点の緯度経度（headerにlon latが必要）が書かれたファイルを用意
3. 指定したい範囲のグリッドサイズ（length）と個数（num）を書いたファイルを用意（ns_set, ew_set, z_set, headerにnum, lengthが必要）
4. 変換先の直交座標系のEPSGコードを調査(https://epsg.io/)
5. MFBを起動

    `$ python mfb_gui.py`

6. GUI上で設定値を更新（Save Settingsボタンを押す）
7. ファイルを作成（Make Filesボタンを押す）
8. ModEMでインバージョン
9. MFBで後処理（震源ファイルにはheader [lon lat depth m]が必要。mはマグニチュードの意味、その他の点を表すファイルにはheader [lon lat height]が必要。）

## インストール

gitからのインストールはインストールしたいディレクトリで以下のコマンドを実行。

    $ git clone https://github.com/r-tnk/MFB.git

## To Do

- 画面サイズに合わせて要素サイズを変更可能にする（現状は、mfb_gui.pyの6行目、sg.set_options(font=('Meiriyo UI', 14)) のfontの数字（fontサイズ）を変更することで画面サイズに合わせてください）

## 開発者

[R. Tanaka](https://www.researchgate.net/profile/Ryo-Tanaka-12)

## 著作権

[MIT](https://github.com/r-tnk/MFB/blob/main/LICENSE)