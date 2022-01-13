import PySimpleGUI as sg                                 # パート 1 - インポート
import mfb

#sg.theme_previewer()
sg.theme('dark')
sg.set_options(font=('Meiriyo UI', 14))

global settings, dicti_vars
layout = [
   [sg.InputText("Choose setting file(*.ini)", key='-file-', enable_events=True,), sg.FileBrowse(key="ini_path")],
   [sg.Combo(values=[''], size=(15,1), key='SECTION', enable_events=True), sg.Checkbox('Create new section'), sg.InputText('Enter name of new section')],
   [sg.T("save_dir", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='save_dir'), sg.InputText("Set directory to save"), sg.FolderBrowse(key="save_dir_set")],
   [sg.T("demfile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='demfile'), sg.InputText("Set file of DEM"), sg.FilesBrowse(file_types=(('ALL FILES', '*,*')), key="demfile_set")],
   [sg.T("seafile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='seafile'), sg.InputText("Set file of bathymetry"), sg.FileBrowse(key="seafile_set")],
   [sg.T("obsfile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='obsfile'), sg.InputText("Set file of observation point"), sg.FileBrowse(key="obsfile_set")],
   [sg.T("origin_lon", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='origin_lon'), sg.InputText("Enter longitude of origin", key='origin_lon_set')],
   [sg.T("origin_lat", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='origin_lat'), sg.InputText("Enter latitude of origin", key='origin_lat_set')],
   [sg.T("catesian", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='cartesian'), sg.InputText("Enter cartesian", key='cartesian_set')],
   [sg.T("ns_set", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='ns_set'), sg.InputText("Set file of ns_set"), sg.FileBrowse(key="ns_set_set")],
   [sg.T("ew_set", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='ew_set'), sg.InputText("Set file of ew_set"), sg.FileBrowse(key="ew_set_set")],
   [sg.T("z_set", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='z_set'), sg.InputText("Set file of z_set"), sg.FileBrowse(key="z_set_set")],
   [sg.T("ns_lim", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='ns_lim'), sg.InputText("Enter ns_lim", key='ns_lim_set')],
   [sg.T("ew_lim", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='ew_lim'), sg.InputText("Enter ew_lim", key='ew_lim_set')],
   [sg.T("z_lim", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='z_lim'), sg.InputText("Enter z_lim", key='z_lim_set')],
   [sg.T("x_min", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='x_min'), sg.InputText("Enter x_min", key='x_min_set')],
   [sg.T("x_max", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='x_max'), sg.InputText("Enter xmax", key='x_max_set')],
   [sg.T("y_min", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='y_min'), sg.InputText("Enter y_min", key='y_min_set')],
   [sg.T("y_max", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='y_max'), sg.InputText("Enter y_max", key='y_max_set')],
   [sg.T("covfile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='covfile'), sg.InputText("Enter name of covfile (.cov)", key='confile_set')],
   [sg.T("covtxt", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='covtxt'), sg.InputText("Enter name of covtxt (.txt)", key='covtxt_set')],
   [sg.T("wsfile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='wsfile'), sg.InputText("Enter name of wsfile (.ws)", key='wsdile_set')],
   [sg.T("smooth", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='smooth'), sg.InputText("Enter smoothing parameter(0 - 1)", key='smooth_set')],
  
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
            window[key].update(config[values['SECTION']][key])

window.close()