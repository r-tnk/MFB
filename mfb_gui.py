import PySimpleGUI as sg                                 # パート 1 - インポート
import mfb

global settings, dicti_vars
layout = [
   [sg.T("Choose setting file(*.ini)"), sg.InputText(), sg.FileBrowse(key="ini_path")],
   [sg.Button('GO'), sg.Button('Cancel')],
]

window = sg.Window("MFBver3.0", layout)
dict_vars = {}
mfb.set_smooth(dict_vars)
section_name = 'SMOOTH5'

# イベントループを使用してウィンドウを表示し、対話する
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'GO':
        mfb.write_ini(values['ini_path'], dict_vars, section_name)

# 画面から削除して終了
window.close()