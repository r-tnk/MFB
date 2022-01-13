import PySimpleGUI as sg                                 # パート 1 - インポート

# ウィンドウの内容を定義する
layout = [  [sg.Text("お名前は何ですか？")],     # パート 2 - レイアウト
            [sg.Input()],
            [sg.Button('はい')] ]
# ウィンドウを作成する
window = sg.Window('ウィンドウタイトル', layout)      # パート 3- ウィンドウ定義
                                                
# ウィンドウを表示し、対話する
event, values = window.read()                   # パート 4- イベントループまたは Window.read 呼び出し

# 収集された情報で何かをする
print('ハロー ', values[0], "PySimpleGUIを試してくれてありがとう!")

# 画面から削除して終了
window.close()    