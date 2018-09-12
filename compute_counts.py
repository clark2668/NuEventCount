# -*- coding: utf-8 -*-
import numpy as np
import sys
import matplotlib.pyplot as plt
from pylab import setp
from matplotlib.pyplot import rcParams
rcParams['mathtext.default'] = 'regular'
from scipy.interpolate import splrep, splev

import constants as const
import tools as tool
import plots as plotter

'''
I want your energy in units of log10(eV)
And your veff in units of cm^3 * steradian
In a CSV file with one header line. See sample_veff.csv as an example.


Use like "python compute_counts.py veff_file.csv"
'''
if(len(sys.argv)<2):
	print "Invalid usage! Use like: 'python compute_counts.py veff_file.csv'"
	print "Aborting!"
	exit()

filename = sys.argv[1]
data = np.genfromtxt(filename,delimiter=',',skip_header=1,names=['energy_logev','veff'])
logeV = data['energy_logev']
veff = data['veff']
aeff = veff/tool.get_Lint(np.power(10.,logeV))
interpolator = splrep(logeV, np.log10(aeff))

livetime = const.SecPerYear
counts=[]
energy_bins=[]
bins = np.arange(15.5,21,0.5)
for bin in bins:
	temp_logev = np.arange(bin,bin+0.5,0.1)
	temp_energy = np.power(10.,temp_logev)
	temp_aeff = np.power(10.,splev(temp_logev, interpolator))
	temp_icecube = tool.get_flux('icecube_thrumu',temp_logev)
	temp_counts = np.trapz(temp_icecube*temp_aeff*livetime,temp_energy)

	counts.append(temp_counts)
	energy_bins.append(np.power(10.,bin))
counts=np.array(counts)
energy_bins=np.array(energy_bins)

fig = plt.figure(figsize=(2.*11,8.5))
ax_veff = fig.add_subplot(1,2,1)
ax_counts = fig.add_subplot(1,2,2)
ax_veff.plot(np.power(10.,logeV),veff,'-o',linewidth=2.0,color='blue',label=r'Sample System')
print counts
n, bins, patches= ax_counts.hist(energy_bins,
									bins=np.power(10.,np.arange(15,22,0.5)),
									weights=counts,
									label=r'IceCube Thru-Mu E$^{-2.19}$: %.2f'%counts.sum(),
									fill=False, 
									stacked=True, 
									histtype='step', 
									edgecolor='blue',
									linewidth=4)
plotter.beautify_veff(ax_veff)
plotter.beautify_counts(ax_counts)
fig.savefig("test.png",edgecolor='none',bbox_inches="tight") #save the figure