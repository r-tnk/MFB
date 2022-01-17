import PySimpleGUI as sg
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

flame1 = sg.Frame('Draw apparent resistivity and phase', [
    [sg.T("Choose datafile", size=(25,1)), sg.InputText("Choose datafile"), sg.FileBrowse(key='datafile')],
    [sg.T("Choose result file (*.dat)", size=(25,1)), sg.InputText("Choose result file (*.dat)"), sg.FileBrowse(key='resfile')],
    [sg.Button('Draw Result')]
])

flame2_1 = sg.Frame("Required items", [
    [sg.T("Choose Save Directory", size=(25,1)), sg.InputText("Choose Save Directory"), sg.FolderBrowse(key='save_dir_post')],
    [sg.T("Choose sealevel file", size=(25,1)), sg.InputText("Choose sealevel file"), sg.FileBrowse(key='slfile')]
], background_color='grey66')

flame2_2 = sg.Frame("Make vtr of resistivity distribution", [
    [sg.T("Choose result file (model file, *.ws)", size=(25,1)), sg.InputText("Choose result file (model file, *.ws)"), sg.FileBrowse(key='wsfile_post')],
    [sg.T("Enter savefile (without extension)", size=(25,1)), sg.InputText("Enter savefile (without extension)", key='vtr')],
    [sg.Button('Make vtr')]
])

flame2_3 = sg.Frame("Make vtk for hypocenters",[
    [sg.T("Choose file of hypocenters", size=(25,1)), sg.InputText("Choose file of hypocenters"), sg.FileBrowse(key='hypofile')],
    [sg.T("Enter savefile (without extension)", size=(25,1)), sg.InputText("Enter savefile (without extension)", key='vtk_hypo')],
    [sg.Button('Make vtk for hypocenters')]
], background_color='grey66')

flame2_4 = sg.Frame("Make vtk for points",[
    [sg.T("Choose file of points", size=(25,1)), sg.InputText("Choose file of points"), sg.FileBrowse(key='pointsfile')],
    [sg.T("Enter savefile (without extension)", size=(25,1)), sg.InputText("Enter savefile (without extension)", key='vtk_point')],
    [sg.Button('Make vtk for points')]
])

flame2 = sg.Frame('Make files for paraview', [
    [flame2_1],
    [flame2_2],
    [flame2_3],
    [flame2_4]
    ])

flame3_1= sg.Frame("Set files and directory",[
    [sg.T("Choose Save Directory", size=(25,1)), sg.InputText("Choose Save Directory"), sg.FolderBrowse(key='save_dir_mdl')],
    [sg.T("Choose file of resistivity model", size=(25,1)), sg.InputText("Choose file of resistivity model"), sg.FileBrowse(key='wsfile_mdl')],
    [sg.T("Choose file of covfile (.txt not .cov)", size=(25,1)), sg.InputText("Choose file of covfile"), sg.FileBrowse(key='covfile_mdl')],
    [sg.T("Enter savefile (*.ws)", size=(25,1)), sg.InputText("Enter savefile (*.ws)", key='ofile_mdl')],
])

flame3_2 = sg.Frame('Set parameters',[
    [sg.T("Enter min and max of NS", size=(20,1)), sg.InputText("min", key='ns_min', size=3), sg.InputText("max", key='ns_max', size=3)],
    [sg.T("Enter min and max of EW", size=(20,1)), sg.InputText("min", key='ew_min', size=3), sg.InputText("max", key='ew_max', size=3)],
    [sg.T("Enter min and max of Z", size=(20,1)), sg.InputText("min", key='z_min', size=3), sg.InputText("max", key='z_max', size=3)],
    [sg.T("Select mode", size=12), sg.Combo(values=['Constant', 'Multiply'], key='-pattern-')],
    [sg.T("Enter constant resistivity value or factor", size=30)],
    [sg.InputText("Enter constant resistivity value or factor", key='cf_num', size=30)]
])

flame3 = sg.Frame('Modify model for sensitivity check',[
    [flame3_1, flame3_2],
    [sg.Button('Modify model')]
    ])


tab2 = sg.Tab('Post-process',[
    [flame1],
    [flame2],
    [flame3]
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

    if event == 'Draw Result':
        mfb.draw_res(values['datafile'], values['resfile'])
        
    if event == 'Make vtr':
        settings_vtr = {
            'wsfile':values['wsfile_post'],
            'vtr':values['vtr'],
            'sl':values['slfile'],
            'save_dir':values['save_dir_post']
        }
        mfb.make_vtr(settings_vtr)

    if event == 'Make vtk for hypocenters':
        mfb.hypo(values['hypofile'], values['save_dir_post'] + '/' + values['vtk_hypo'])

    if event == 'Make vtk for points':
        mfb.point2vtk(values['pointsfile'], values['slfile'], values['save_dir_post'] + '/' + values['vtk_point'])

    if event == 'Modify model':
        if values['-pattern-'] == 'Multiply':
            const = False
        else:
            const = True    
        settings_mdl = {
            'save_dir': values['save_dir_mdl'],
            'in_wsfile' : values['wsfile_mdl'],
            'wsfile' : values['ofile_mdl'],
            'covfile' : values['covfile_mdl'],
            'ns_s': values['ns_min'],
            'ns_e':values['ns_max'],
            'ew_s':values['ew_min'],
            'ew_e':values['ew_max'],
            'z_s':values['z_min'],
            'z_e':values['z_max'],
            'const':const,
            'factor':values['cf_num']
        }
        mfb.mod_mdl(settings_mdl)

window.close()