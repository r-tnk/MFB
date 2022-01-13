import PySimpleGUI as sg                                 # パート 1 - インポート
import mfb

global settings, dicti_vars
layout = [
   [sg.T("Choose setting file(*.ini)"), sg.InputText("Choose setting file(*.ini)", key='-file-', enable_events=True), sg.FileBrowse(key="ini_path")],
   [sg.Combo(values=[''], key='SECTION')],
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

    if event == '-file-':
        config = mfb.read_ini(values['ini_path'])
        print(config.sections())
        window.find_element('SECTION').Update(values=config.sections())

# 画面から削除して終了
window.close()