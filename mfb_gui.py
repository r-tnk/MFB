import PySimpleGUI as sg                                 # パート 1 - インポート
import mfb

#sg.theme_previewer()
sg.theme('dark')
sg.set_options(font=('Meiriyo UI', 14))

tab1 = sg.Tab('Pre-Process', [
   [sg.InputText("Choose setting file(*.ini)", key='-file-', enable_events=True,), sg.FileBrowse(key="ini_path")],
   [sg.Combo(values=[''], size=(15,1), key='-section-', enable_events=True), sg.Checkbox('Create new section', key='newsec'), sg.InputText('Enter name of new section', key='sec_set')],
   [sg.T("save_dir", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='save_dir'), sg.Checkbox('Update to', key='save_dir_up'), sg.InputText("Set directory to save"), sg.FolderBrowse(key="save_dir_set")],
   [sg.T("demfile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='demfile'), sg.Checkbox('Update to', key='demfile_up'), sg.InputText("Set file of DEM"), sg.FileBrowse(key="demfile_set")],
   [sg.T("seafile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='seafile'), sg.Checkbox('Update to', key='seafile_up'), sg.InputText("Set file of bathymetry"), sg.FileBrowse(key="seafile_set")],
   [sg.T("obsfile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='obsfile'), sg.Checkbox('Update to', key='obsfile_up'), sg.InputText("Set file of observation point"), sg.FileBrowse(key="obsfile_set")],
   [sg.T("origin_lon", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='origin_lon'), sg.Checkbox('Update to', key='origin_lon_up'), sg.InputText("Enter longitude of origin", key='origin_lon_set')],
   [sg.T("origin_lat", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='origin_lat'), sg.Checkbox('Update to', key='origin_lat_up'), sg.InputText("Enter latitude of origin", key='origin_lat_set')],
   [sg.T("catesian", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='cartesian'), sg.Checkbox('Update to', key='cartesian_up'), sg.InputText("Enter cartesian", key='cartesian_set')],
   [sg.T("ns_set", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='ns_set'), sg.Checkbox('Update to', key='ns_set_up'), sg.InputText("Set file of ns_set"), sg.FileBrowse(key="ns_set_set")],
   [sg.T("ew_set", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='ew_set'), sg.Checkbox('Update to', key='ew_set_up'), sg.InputText("Set file of ew_set"), sg.FileBrowse(key="ew_set_set")],
   [sg.T("z_set", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='z_set'), sg.Checkbox('Update to', key='z_set_up'), sg.InputText("Set file of z_set"), sg.FileBrowse(key="z_set_set")],
   [sg.T("ns_lim", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='ns_lim'), sg.Checkbox('Update to', key='ns_lim_up'), sg.InputText("Enter ns_lim", key='ns_lim_set')],
   [sg.T("ew_lim", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='ew_lim'), sg.Checkbox('Update to', key='ew_lim_up'), sg.InputText("Enter ew_lim", key='ew_lim_set')],
   [sg.T("z_lim", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='z_lim'), sg.Checkbox('Update to', key='z_lim_up'), sg.InputText("Enter z_lim", key='z_lim_set')],
   [sg.T("x_min", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='x_min'), sg.Checkbox('Update to', key='x_min_up'), sg.InputText("Enter x_min", key='x_min_set')],
   [sg.T("x_max", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='x_max'), sg.Checkbox('Update to', key='x_max_up'), sg.InputText("Enter xmax", key='x_max_set')],
   [sg.T("y_min", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='y_min'), sg.Checkbox('Update to', key='y_min_up'), sg.InputText("Enter y_min", key='y_min_set')],
   [sg.T("y_max", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='y_max'), sg.Checkbox('Update to', key='y_max_up'), sg.InputText("Enter y_max", key='y_max_set')],
   [sg.T("covfile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='covfile'), sg.Checkbox('Update to', key='covfile_up'), sg.InputText("Enter name of covfile (.cov)", key='covfile_set')],
   [sg.T("covtxt", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='covtxt'), sg.Checkbox('Update to', key='covtxt_up'), sg.InputText("Enter name of covtxt (.txt)", key='covtxt_set')],
   [sg.T("wsfile", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='wsfile'), sg.Checkbox('Update to', key='wsfile_up'), sg.InputText("Enter name of wsfile (.ws)", key='wsfile_set')],
   [sg.T("smooth", text_color='black', background_color='azure', size=(17,1), justification='center'), sg.Text(size=(30,1), key='smooth'), sg.Checkbox('Update to', key='smooth_up'), sg.InputText("Enter smoothing parameter(0 - 1)", key='smooth_set')],
  
   [sg.Button('Save Settings'), sg.Button('Make files'), sg.Button('Done')],
])

tab2 = sg.Tab('Post-process',[
    [sg.InputText("Choose setting file(*.ini)", key='-file-', enable_events=True,), sg.FileBrowse(key="ini_path")],
    [sg.Combo(values=[''], size=(15,1), key='-section-', enable_events=True), sg.Checkbox('Create new section', key='newsec'), sg.InputText('Enter name of new section', key='sec_set')]
])

layout = [[sg.TabGroup ([[tab1 ,tab2]])]]
window = sg.Window("MFBver3.0", layout)
dict_vars ={}

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Done':
        break

    if event == '-file-':
        config = mfb.read_ini(values['ini_path'])
        window.find_element('-section-').Update(values=config.sections())
    
    if event == '-section-':
        section = values['-section-']
        for key in config[values['-section-']]:
            window[key].update(config[values['-section-']][key])

    if event == 'Save Settings':
        if values['newsec']:
            section = values['sec_set']
        else:
            section = values['-section-']
        for key in config[values['-section-']]:
            if values[key + '_up']:
                dict_vars[key] = values[key + '_set']
            else:
                dict_vars[key] = config[values['-section-']][key]

        mfb.write_ini(values['ini_path'], dict_vars, section)

    if event == 'Make files':
        config = mfb.read_ini(values['ini_path'])
        settings = config[section]
        mfb.preprocess(settings)
        

            

window.close()