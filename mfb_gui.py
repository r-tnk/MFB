import PySimpleGUI as sg                                 # パート 1 - インポート
import mfb

global settings, dicti_vars
layout = [
   [sg.InputText("Choose setting file(*.ini)", key='-file-', enable_events=True), sg.FileBrowse(key="ini_path")],
   [sg.Combo(values=[''], size=(20,1), key='SECTION', enable_events=True)],
   [sg.Button('GO'), sg.Button('Cancel')],
]

window = sg.Window("MFBver3.0", layout)
dict_vars = {}
mfb.set_smooth(dict_vars)
section_name = 'SMOOTH5'

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break

    if event == '-file-':
        config = mfb.read_ini(values['ini_path'])
        print(config.sections())
        window.find_element('SECTION').Update(values=config.sections())
    
    if event == 'SECTION':
        for key in config[values['SECTION']]:
            print(key, config[values['SECTION']][key])

window.close()