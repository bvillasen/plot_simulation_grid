import os, sys
import numpy as np
import matplotlib.pyplot as plt
import pickle
from data_thermal_history import *

import matplotlib
matplotlib.use('Agg') 
matplotlib.font_manager.findSystemFonts(fontpaths=['/home/bruno/Downloads'], fontext='ttf')
matplotlib.rcParams['font.sans-serif'] = "Helvetica"
matplotlib.rcParams['font.family'] = "sans-serif"
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['mathtext.rm'] = 'serif'


data_file = open( 'scale_HeII_T0.pkl', 'rb')
data_grid = pickle.load( data_file )

sim_ids = data_grid.keys()


data_sets = [ data_thermal_history_Gaikwad_2020a, data_thermal_history_Gaikwad_2020b ]


error_colors = [ 'C9', 'C0', 'C1']
font_size = 15

nrows = 1
ncols = 1
fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10*ncols,8*nrows))

for sim_id in sim_ids:
  z = data_grid[sim_id]['z']
  T0 = data_grid[sim_id]['T0']
  scale_He = data_grid[sim_id]['parameters']['scale_He']
  label = r'$\beta_{HeII}$' + ' $= {0}$'.format(scale_He)
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

ax.set_ylabel( r'$T_0$', fontsize=font_size  )
ax.set_xlabel( r'$z$', fontsize=font_size )
leg = ax.legend(loc=1, frameon=False, fontsize=font_size)
ax.set_xlim( 2, 12 )
ax.set_ylim( 3000, 18000)

ax.tick_params(axis='both', which='major', direction='in' )
ax.tick_params(axis='both', which='minor', direction='in' )

figure_name = 'grid_T0.png'
fig.savefig( figure_name, bbox_inches='tight', dpi=300 )
print( f'Saved Figure: {figure_name}' )

