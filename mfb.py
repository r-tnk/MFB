from mimetypes import init
from os import name
import pandas as pd
import pyproj
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from pyevtk.hl import gridToVTK
from pyevtk.hl import pointsToVTK
import configparser
import matplotlib as mpl

def main():
    settings = '~/settings.ini'
    preprocess(settings)
    
def preprocess(settings):
    ###Pre-process###
    dem, sea_level = get_dem(settings)
    dem = cor_dem(dem, settings)
    ns0, ew0, z0, ns_set, ew_set, z_set, ns_corner, ew_corner, z_corner = set_xyz(settings)
    zblocks, block_depth, sea_level = cal_zblocks(settings, ns_corner, ew_corner, z_corner, dem, sea_level)
    obs = cal_obs_point(settings, ns_corner, ew_corner, block_depth)
    plot_fig(settings, ns_corner, ew_corner, block_depth, sea_level, obs)
    rho, msk = get_ws_cov(zblocks, ns_set, ew_set, z_set, sea_level, z_corner)
    save_ws(settings, ns_set, ew_set, z_set, ns_corner, ew_corner, z_corner, rho)
    save_cov(settings, ns_set, ew_set, z_set, msk)
    
def mod_mdl(settings):
    res = settings['in_wsfile']
    ns0, ew0, z0, ns_set, ew_set, z_set, ns_corner, ew_corner, z_corner, ws = read_mdl(res)
    cov_file = settings['covfile']
    cov = read_cov(cov_file)
    ws = mdl2mdl(ws, cov, settings)
    save_ws(settings, ns_set, ew_set, z_set, ns_corner, ew_corner, z_corner, ws)
    
def make_vtr(settings):
    res = settings['wsfile']
    ns0, ew0, z0, ns_set, ew_set, z_set, ns_corner, ew_corner, z_corner, ws = read_mdl(res)    
    vtr = settings['save_dir'] + '/' + settings['vtr']
    sl = settings['sl']
    sea_level = read_sl(sl)
    rho2vtk(ws, ns_corner, ew_corner, z_corner, sea_level, vtr)

def draw_res(datafile, resfile):
    head = ('T', 'STATION', 'a', 'b', 'NS', 'EW', 'Z', 'COMPONENT', 'real', 'imag', 'err')
    types = {'T':float, 'STATION':str, 'a':float, 'b':float, 'NS':float, 'EW':float, 'Z':float, 'COMPONENT':str, 'real':float, 'imag':float, 'err':float}
    data = pd.read_table(datafile, delim_whitespace = True, names=head, dtype=types, skiprows=8)
    res = pd.read_table(resfile, delim_whitespace = True, names=head, dtype=types, skiprows=8)
    calc_rho(data)
    calc_rho(res)
    data = data.sort_values('T')
    res = res.sort_values('T')
    xmin = data['T'].min()*0.5
    xmax = data['T'].max()*2.0
    ymin = data['rho'].min()*0.5
    ymax = data['rho'].max()*2.0
    g = data.groupby('STATION')
    line_col = {'ZXX':'green', 'ZYY': 'magenta', 'ZXY':'red', 'ZYX':'blue'}
    com_fmt = {'ZXX':'go', 'ZYY': 'mo', 'ZXY':'ro', 'ZYX':'bo'}
    comp_list = ('ZXX', 'ZYY', 'ZXY', 'ZYX')
    fig, ax = plt.subplots((len(g)//6 + 1) * 2, 6)
    fig.suptitle('Cal vs. Obs')
    fig.subplots_adjust(hspace=0.4, wspace=0.1)
    i =0
    for name, group in g:
        row = (i//6)*2
        col = i%6
        for comp in comp_list:
            ax[row][col].plot(res[(res['STATION'] == name) & (res['COMPONENT'] == comp)]['T'], res[(res['STATION'] == name) & (res['COMPONENT'] == comp)]['rho'], line_col[comp], lw=1.0, alpha = 0.7)
            ax[row][col].errorbar(data[(data['STATION'] == name) & (data['COMPONENT'] == comp)]['T'], data[(data['STATION'] == name) & (data['COMPONENT'] == comp)]['rho'], yerr = data[(data['STATION'] == name) & (data['COMPONENT'] == comp)]['rho_err'], fmt=com_fmt[comp], markersize=2, capsize=4, ecolor=line_col[comp])     
            ax[row+1][col].plot(res[(res['STATION'] == name) & (res['COMPONENT'] == comp)]['T'], res[(res['STATION'] == name) & (res['COMPONENT'] == comp)]['phase'], line_col[comp], lw=1.0, alpha = 0.7)
            ax[row+1][col].errorbar(data[(data['STATION'] == name) & (data['COMPONENT'] == comp)]['T'], data[(data['STATION'] == name) & (data['COMPONENT'] == comp)]['phase'], yerr = data[(data['STATION'] == name) & (data['COMPONENT'] == comp)]['phase_err'], fmt=com_fmt[comp], markersize=2, capsize=4, ecolor=line_col[comp])     
           
        ax[row][col].set_xlim(xmin,xmax)
        ax[row][col].set_xscale('log')
        ax[row][col].set_ylim(ymin,ymax)
        ax[row][col].set_yscale('log')
        ax[row][col].yaxis.set_major_locator(mpl.ticker.LogLocator(numticks=13))
        ax[row][col].xaxis.set_major_locator(mpl.ticker.LogLocator(numticks=13))
        ax[row+1][col].set_xlim(xmin,xmax)
        ax[row+1][col].set_xscale('log')
        ax[row+1][col].xaxis.set_major_locator(mpl.ticker.LogLocator(numticks=13))
        ax[row+1][col].set_ylim(-180,180)
        ax[row+1][col].set_yticks( np.arange(-180, 181, 60))
        ax[row][col].set_title(name)

        if row == (len(g)//6 + 1) * 2 -2 and col == 0:
            ax[row][col].tick_params(labelbottom=False, labelright=False, labeltop=False)
            ax[row+1][col].tick_params(labelright=False, labeltop=False)
            ax[row][col].set_ylabel("Apparent resistivity\n[log \u03a9 m]")
            ax[row+1][col].set_ylabel("Phase")
            ax[row+1][col].set_xlabel("Period [s]")
        elif row == (len(g)//6 + 1) * 2 -2:
            ax[row][col].tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
            ax[row+1][col].tick_params(labelleft=False, labelright=False, labeltop=False)
            ax[row+1][col].set_xlabel("Period [s]")
        elif col == 0:
            ax[row][col].tick_params(labelbottom=False, labelright=False, labeltop=False)
            ax[row+1][col].tick_params(labelbottom=False, labelright=False, labeltop=False)
            ax[row][col].set_ylabel("Apparent resistivity\n[log \u03a9 m]")
            ax[row+1][col].set_ylabel("Phase")
        else:
            ax[row][col].tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
            ax[row+1][col].tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
        i += 1

    plt.show()

def calc_rho(data):    
    data['amp'] = np.sqrt(data['real'] * data['real'] + data['imag'] * data['imag'])
    data['rho'] = 0.2 * data['amp'] * data['amp'] * data['T']
    data['phase'] = np.degrees(np.arctan2(data['imag'], data['real']))
    data['rho_err'] = 0.4 * data['amp'] * data['err'] * data['T']
    data['phase_err'] = np.degrees(np.arcsin(data['err']/data['amp']))
    return data

def read_ini(config_path):
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')
    return config

def write_ini(config_path, dict_vars, section_name):
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')
    #config[section_name] = {}
    for k in dict_vars:
        config[section_name][k] = dict_vars[k]

    with open(config_path, 'w') as f:
        config.write(f)

def read_ini(config_path):
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')
    return config

def hypo(fin, fout):
    hfile = fin
    hypoth = pd.read_table(hfile, delim_whitespace = True, names=('EW', 'NS', 'depth', 'm'), dtype=float)
    x = hypoth['EW'].to_numpy()
    y = hypoth['NS'].to_numpy()
    z = hypoth['depth'].to_numpy()
    m = hypoth['m'].to_numpy()
    pointsToVTK(fout, x, y, z, data={'magnitude':m})

def point2vtk(pointsfile, slfile, fout):
    sea_level = read_sl(slfile)
    type = {'EW':float, 'NS':float, 'depth':float}
    point = pd.read_table(pointsfile, delim_whitespace = True,  dtype=type)
    x = point['EW'].to_numpy()
    y = point['NS'].to_numpy()
    z = sea_level - point['depth'].to_numpy()
    print(x,y,z)
    pointsToVTK(fout, x, y, z) 

def read_sl(sl):
    with open(sl, 'r') as f:
        sea_level = float(f.read())
    return sea_level

def rho2vtk(ws, ns_corner, ew_corner, z_corner, sea_level, vtr):
    for k in range(ws.shape[2]):
        ws[:,:,k] = np.fliplr(ws[:,:,k].T)
    gridToVTK(vtr, ew_corner, ns_corner, sea_level-z_corner, cellData = {"resistivity" : np.log10(np.exp(ws))})

def mdl2mdl(ws, cov, change_condition):
    cov_trans = np.empty_like(ws)
    for k in range(ws.shape[2]):
        cov_trans[0:ws.shape[0],:,k] = np.flipud(cov[ws.shape[0]*(k):ws.shape[0]*(k+1),:])
    ns_s = int(change_condition['ns_s'])
    ns_e = int(change_condition['ns_e'])
    ew_s = int(change_condition['ew_s'])
    ew_e = int(change_condition['ew_e'])
    z_s = int(change_condition['z_s'])
    z_e = int(change_condition['z_e'])
    const = change_condition['const']
    factor = float(change_condition['factor'])
    if const:
        ws_mod = np.where(cov_trans == 1, math.log(factor), ws)
    else:
        ws_mod = np.where(cov_trans == 1, np.log(np.exp(ws)*factor), ws)
    ws[ns_s:ns_e, ew_s:ew_e, z_s:z_e] = ws_mod[ns_s:ns_e, ew_s:ew_e, z_s:z_e]
    return(ws)

def read_cov(fin):
    df = pd.read_table(fin, header=None, delim_whitespace = True, engine='python')
    cov = df.to_numpy()
    return cov

def read_mdl(fin):
    ns_set = pd.read_table(fin, header=None, skiprows=lambda x: x not in [2, 5], delim_whitespace = True)
    ew_set = pd.read_table(fin, header=None, skiprows=lambda x: x not in [3, 5], delim_whitespace = True)
    z_set = pd.read_table(fin, header=None, skiprows=lambda x: x not in [4, 5], delim_whitespace = True)
    rho = pd.read_table(fin, header=None, skiprows=6, skipfooter=3, delim_whitespace = True, engine='python')
    rho = rho.to_numpy()
    ns_set = ns_set.to_numpy()
    ew_set = ew_set.to_numpy()
    z_set = z_set.to_numpy()
    lines = rho.shape[0] + z_set.shape[1] + 5
    lbz = pd.read_table(fin, header=None, skiprows=lines, skipfooter=1, delim_whitespace = True, engine='python')
    ns0 = lbz[0][0]
    ew0 = lbz[1][0]
    z0 = lbz[2][0]
    ns_corner = set_corner(ns0, ns_set.T)
    ew_corner = set_corner(ew0, ew_set.T)
    z_corner = set_corner(z0, z_set.T)
    ws = np.empty((ns_set.shape[1], ew_set.shape[1], z_set.shape[1]))
    for k in range(z_set.shape[1]):
        ws[0:ns_set.shape[1],:,k] = np.flipud(rho[ns_set.shape[1]*(k):ns_set.shape[1]*(k+1),:].T)
    return(ns0, ew0, z0, ns_set.reshape(ns_set.shape[1]), ew_set.reshape(ew_set.shape[1]), z_set.reshape(z_set.shape[1]), ns_corner, ew_corner, z_corner, ws)
    
def get_ws_cov(zblocks, ns_set, ew_set, z_set, sea_level, z_corner):
    cov = {'land':1, 'air':0, 'sea':9}
    ws = {'land':math.log(100), 'air': math.log(1e8), 'sea':math.log(0.3)}
    rho = np.empty((len(ns_set), len(ew_set), len(z_set)))
    msk = np.empty((len(ns_set), len(ew_set), len(z_set)))
    for k in range(len(z_set)):
            if(z_corner[k+1] < sea_level):
                rho[:,:,k] = np.where(zblocks <= k, ws['land'], ws['air'])
                msk[:,:,k] = np.where(zblocks <= k, cov['land'], cov['air'])
            else:
                rho[:,:,k] = np.where(zblocks <= k, ws['land'], ws['sea'])
                msk[:,:,k] = np.where(zblocks <= k, cov['land'], cov['sea'])
    return(rho, msk)

def save_cov(settings,ns_set, ew_set, z_set, msk):
    covfile = settings['save_dir'] + '/' + settings['covfile']
    backcov = settings['save_dir'] + '/' + settings['covtxt']
    with open(covfile, 'w') as f:
        smooth = float(settings['smooth'])
        ns_smooth = np.full(z_set.shape, smooth)
        ew_smooth = np.full(z_set.shape, smooth)
        head = """ +-----------------------------------------------------------------------------+
 | This file defines model covariance for a recursive autoregression scheme.   |
 | The model space may be divided into distinct areas using integer masks.     |
 | Mask 0 is reserved for air; mask 9 is reserved for ocean. Smoothing between |
 | air, ocean and the rest of the model is turned off automatically. You can   |
 | also define exceptions to override smoothing between any two model areas.   |
 | To turn off smoothing set it to zero. This header is 16 lines long.         |
 | 1. Grid dimensions excluding air layers (Nx, Ny, NzEarth)                   |
 | 2. Smoothing in the X direction (NzEarth real values)                       |
 | 3. Smoothing in the Y direction (NzEarth real values)                       |
 | 4. Vertical smoothing (1 real value)                                        |
 | 5. Number of times the smoothing should be applied (1 integer >= 0)         |
 | 6. Number of exceptions (1 integer >= 0)                                    |
 | 7. Exceptions in the form e.g. 2 3 0. (to turn off smoothing between 3 & 4) |
 | 8. Two integer layer indices and Nx x Ny block of masks, repeated as needed.|
 +-----------------------------------------------------------------------------+\n """
        f.write(head)
        f.write('\n ')
        f.write('%3d %3d %3d\n ' %(int(len(ns_set)), int(len(ew_set)), int(len(z_set))))
        f.write('\n ')
        np.savetxt(f, ns_smooth[None], fmt = '%4.2f', newline = '\n ')
        f.write('\n ')
        np.savetxt(f, ew_smooth[None], fmt = '%4.2f', newline = '\n ')
        f.write('\n ')
        f.write('%4.2f\n ' % smooth)
        f.write('\n ')
        f.write(' 1\n ')
        f.write('\n ')
        f.write(' 0\n ')
        f.write('\n ')
        for k in range(len(z_set)):
            msk[:,:,k] = np.flipud(msk[:,:,k])
            f.write('%2d %2d\n ' % (k+1, k+1))
            np.savetxt(f, msk[:,:,k], fmt = '%2d', newline = '\n ')
            f.write('\n ')
    with open(backcov, 'w') as f:
        f.write('\n ')
        for k in range(len(z_set)):
            np.savetxt(f, msk[:,:,k], fmt = '%2d', newline = '\n ')
            f.write('\n ')

def save_ws(settings,ns_set, ew_set, z_set, ns_corner, ew_corner, z_corner, rho):
    wsfile = settings['save_dir'] + '/' + settings['wsfile']
    with open(wsfile, 'w') as f:
        f.write(' #3D MT model\n')
        f.write(' %3d %3d %3d   0 LOGE\n ' %(int(len(ns_set)), int(len(ew_set)), int(len(z_set))))
        np.savetxt(f, ns_set[None], fmt = '%9.2f', newline = '\n ')
        np.savetxt(f, ew_set[None], fmt = '%9.2f', newline = '\n ')
        np.savetxt(f, z_set[None], fmt = '%9.2f', newline = '\n ')
        f.write('\n ')
        for k in range(len(z_set)):
            rho[:,:,k] = np.flipud(rho[:,:,k])
            np.savetxt(f, rho[:,:,k].T, fmt = '%12.5E', newline = '\n ')
            f.write('\n ')
        f.write('%11.3f %11.3f %11.3f\n ' % (ns_corner[0], ew_corner[0], z_corner[0]))
        f.write('0.000\n ')

def cal_obs_point(settings, ns_corner, ew_corner, block_depth):   
    obs_file = settings['obsfile']
    obs = pd.read_table(obs_file, delim_whitespace = True, names=('lon', 'lat'))
    cor_dem(obs, settings)
    for index, row in obs.iterrows():
        j = int(np.where(ew_corner >= row['EW'])[0][0])
        i = int(np.where(ns_corner >= row['NS'])[0][0])
        obs.at[index, 'EW_reloc'] = (ew_corner[j-1] + ew_corner[j])/2.
        obs.at[index, 'NS_reloc'] = (ns_corner[i-1] + ew_corner[i])/2.
        obs.at[index, 'depth'] = block_depth[i-1,j-1]
    obscor_file = obs_file[:-4] + 'cor.txt'
    obs.to_csv(obscor_file, sep=' ', float_format="%.3f", )
    return(obs)

def plot_fig(settings, ns_corner, ew_corner, block_depth, sea_level, obs):
    fig, ax = plt.subplots(figsize=(15, 15))
    cs = ax.pcolormesh(ns_corner, ew_corner, block_depth, cmap='gist_earth_r', edgecolors="w", linewidth=0.01)
    ax.set_xlim([float(settings['x_min']),float(settings['x_max'])])
    ax.set_ylim([float(settings['y_min']),float(settings['y_max'])])
    fig.colorbar(cs, label = 'depth [m]')
    ax.text(0.0, 1.05, "sea_level = %.1f m" % (sea_level), ha='left', transform=ax.transAxes)
    sns.scatterplot(data=obs, x='EW_reloc', y='NS_reloc', ax=ax)
    ax.set_xlabel('EW [m]')
    ax.set_ylabel('NS [m]')
    ax.set_aspect('equal')
    plt.show()

def cal_zblocks(settings, ns_corner, ew_corner, z_corner, dem, sea_level):
    depth = np.empty((len(ns_corner)-1, len(ew_corner)-1))
    for i in range(len(ew_corner)-1):
        for j in range(len(ns_corner)-1):
            depth[j,i] = dem[(dem['EW'] > ew_corner[i]) & (dem['EW'] < ew_corner[i+1]) & (dem['NS'] > ns_corner[j]) & (dem['NS'] < ns_corner[j+1])]['depth'].mean()
    df = pd.DataFrame(depth)
    df_inter = df.interpolate(limit_direction='both')
    df = df_inter.interpolate(limit_direction='both', axis=1)
    depth = df.to_numpy()
    sea_level = sea_level - np.min(depth)
    depth = depth - np.min(depth)
    zblocks = np.empty_like(depth)
    block_depth = np.empty_like(depth)
    for i in range(len(ew_corner)-1):
        for j in range(len(ns_corner)-1):
            zblocks[j,i] = np.where(z_corner >= depth[j,i])[0][0]
            block_depth[j,i] = z_corner[int(zblocks[j,i])]
    with open(settings['save_dir'] + '/sl.txt', 'w') as f:
        f.write('%.3f' % sea_level)
    return(zblocks, block_depth, sea_level)            

def set_xyz(settings):
    ns_set = np.empty(0)
    ew_set = np.empty(0)
    z_set = np.empty(0)
    ns = pd.read_table(settings['ns_set'], delim_whitespace = True)
    for index, row in ns.iterrows():
        ns_set = np.append(ns_set, np.full(int(row['num']), float(row['length'])))

    ew = pd.read_table(settings['ew_set'], delim_whitespace = True)
    for index, row in ew.iterrows():
        ew_set = np.append(ew_set, np.full(int(row['num']), float(row['length'])))

    z = pd.read_table(settings['z_set'], delim_whitespace = True)
    for index, row in z.iterrows():
        z_set = np.append(z_set, np.full(int(row['num']), float(row['length'])))
    
    ns_lim = float(settings['ns_lim'])
    ew_lim = float(settings['ew_lim'])
    z_lim = float(settings['z_lim'])

    znum0 = z_set.size
    z0 = z_set[-1]
    ns_set = cal_lim(ns_lim, ns_set)
    ew_set = cal_lim(ew_lim, ew_set)
    while(z_lim > z_set.sum()):
        z_set = np.append(z_set, z0 * np.exp(z_set.size - znum0 + 1))
    ns0 = -(ns_set.sum())
    ew0 = -(ns_set.sum())
    z0 = 0.
    ns_set = np.concatenate([np.flip(ns_set), ns_set])
    ew_set = np.concatenate([np.flip(ew_set), ew_set])
    ns_corner = set_corner(ns0, ns_set)
    ew_corner = set_corner(ew0, ew_set)
    z_corner = set_corner(z0, z_set)
    return(ns0, ew0, z0, ns_set, ew_set, z_set, ns_corner, ew_corner, z_corner)

def set_corner(xyz0, xyzset):
    corner = np.empty(len(xyzset)+1)
    corner[0] = xyz0
    for i in range(len(xyzset)):
        corner[i+1] = xyz0 + xyzset[:i+1].sum()
    return(corner)

def cal_lim(lim, xyset):
    while(lim > xyset.sum()):
        xyset = np.append(xyset, xyset[-1]*1.4)
    return(xyset)
        
def cor_dem(dem, settings):
    origin = {'lon': float(settings['origin_lon']), 'lat': float(settings['origin_lat'])}
    wgs84 = pyproj.Proj(init='EPSG:4326')
    cartesian = pyproj.Proj(init=settings['cartesian'])
    x, y = pyproj.transform(wgs84, cartesian, dem['lon'].values, dem['lat'].values, always_xy=True)
    dem['EW'] = x
    dem['NS'] = y
    origin_x, origin_y = pyproj.transform(wgs84, cartesian, origin['lon'], origin['lat'], always_xy=True)
    dem['EW'] = dem['EW'] - origin_x
    dem['NS'] = dem['NS'] - origin_y
    return dem
    
def get_dem(settings):
    sea_file = settings['seafile']
    dem_file = settings['demfile']
    local_dem = pd.read_table(dem_file, delim_whitespace = True, names=('lon', 'lat', 'hight'))
    sea_dem = pd.read_table(sea_file, delim_whitespace = True, names=('q', 'lat', 'lon', 'depth'))
    local_dem = local_dem[local_dem.hight != -9999.00]
    sea_level = local_dem['hight'].max()
    local_dem['depth'] = -local_dem['hight'] + sea_level
    sea_dem['depth'] = sea_dem['depth'] + sea_level
    dem = pd.merge(local_dem, sea_dem, how='outer')
    return (dem,sea_level)

if __name__ == "__main__":
    main()