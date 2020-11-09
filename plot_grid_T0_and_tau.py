import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pickle
from data_thermal_history import *
from data_optical_depth import *

import matplotlib
matplotlib.use('Agg') 
matplotlib.rcParams['font.family'] = "sans-serif"
matplotlib.rcParams['font.sans-serif'] = "Helvetica"
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['mathtext.rm'] = 'serif'


plot_param = 'scale_H'
# plot_param = 'scale_He'

if plot_param == 'scale_H': data_file = open( 'scale_H_T0.pkl', 'rb')
if plot_param == 'scale_He': data_file = open( 'scale_HeII_T0.pkl', 'rb')
data_grid = pickle.load( data_file )

sim_ids = data_grid.keys()


data_sets = [ data_thermal_history_Gaikwad_2020a, data_thermal_history_Gaikwad_2020b ]


error_colors = [ 'C9', 'C0', 'C1']
font_size = 18
legend_font_size = 15

nrows = 1
ncols = 1
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10*ncols,8*nrows))

for sim_id in sim_ids:
  z = data_grid[sim_id]['z']
  T0 = data_grid[sim_id]['T0']
  param_val = data_grid[sim_id]['parameters'][plot_param]
  if plot_param == 'scale_H': label_param = r'$\beta_{HI}$' 
  if plot_param == 'scale_He': label_param = r'$\beta_{HeII}$' 
  label =  label_param + ' $= {0}$'.format(param_val)
  ax.plot( z, T0 , label=label, zorder=1 )


for i, data_set in enumerate( data_sets ):
  data_name = data_set['name']
  data_x = data_set['z']
  data_mean = data_set['T0'].astype(np.float) 
  data_error_p = data_set['T0_sigma_plus']
  data_error_m = data_set['T0_sigma_minus']
  data_error = np.array([ data_error_m, data_error_p ]).astype(np.float) 
  ax.errorbar( data_x, data_mean, yerr=data_error, fmt='none',  alpha=0.8, ecolor= error_colors[i], zorder=2)
  ax.scatter( data_x, data_mean, label=data_name, alpha=0.8, color= error_colors[i], zorder=2) 

ax.set_ylabel( r'$T_0 \,\,\, [ \, \mathrm{K}\,]$', fontsize=font_size  )
ax.set_xlabel( r'$z$', fontsize=font_size )
leg = ax.legend(loc=1, frameon=False, fontsize=legend_font_size)
ax.set_xlim( 2, 12 )
ax.set_ylim( 3000, 18000)

ax.tick_params(axis='both', which='major', direction='in', labelsize=12 )
ax.tick_params(axis='both', which='minor', direction='in' )

figure_name = f'grid_T0_{plot_param}.png'
fig.savefig( figure_name, bbox_inches='tight', dpi=300 )
print( f'Saved Figure: {figure_name}' )







nrows = 1
ncols = 1
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10*ncols,8*nrows))



data_sets = [ data_optical_depth_Boera_2019, data_optical_depth_Becker_2013, data_optical_depth_Bosman_2018 ]
for i,data_set in enumerate(data_sets):
  data_name = data_set['name']
  data_x = data_set['z']
  data_mean = data_set['tau'].astype(np.float) 
  data_error_p = data_set['tau_sigma_p']
  data_error_m = data_set['tau_sigma_m']
  data_error = np.array([ data_error_m, data_error_p ]).astype(np.float) 
  ax.errorbar( data_x, data_mean, yerr=data_error, fmt='none',  alpha=1, ecolor= error_colors[i], zorder=2)
  ax.scatter( data_x, data_mean, label=data_name, alpha=1, color= error_colors[i], zorder=2) 


for sim_id in sim_ids:
  z = data_grid[sim_id]['z']
  F = data_grid[sim_id]['F_mean']
  tau = - np.log( F )
  param_val = data_grid[sim_id]['parameters'][plot_param]
  if plot_param == 'scale_H': label_param = r'$\beta_{HI}$' 
  if plot_param == 'scale_He': label_param = r'$\beta_{HeII}$' 
  label =  label_param + ' $= {0}$'.format(param_val)
  ax.plot( z, tau, label=label, zorder=1 )




ax.set_ylabel( r'$\tau_{eff}$', fontsize=font_size  )
ax.set_xlabel( r'$z$', fontsize=font_size )
leg = ax.legend(loc=2, frameon=False, fontsize=legend_font_size)
ax.set_xlim( 2, 6 )
ax.set_yscale('log')
ax.set_ylim( 0.1, 8 )

ax.tick_params(axis='both', which='major', direction='in', labelsize=12 )
ax.tick_params(axis='both', which='minor', direction='in' )


figure_name = f'grid_tau_{plot_param}.png'
fig.savefig( figure_name, bbox_inches='tight', dpi=300 )
print( f'Saved Figure: {figure_name}' )
