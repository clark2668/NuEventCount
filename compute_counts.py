# -*- coding: utf-8 -*-
import numpy as np
import sys
import matplotlib.pyplot as plt
from pylab import setp
from matplotlib.pyplot import rcParams
rcParams['mathtext.default'] = 'regular'

import constants as const
import tools as tool
import fluxes as flux

def compute_counts():

	'''
	I want your energy in units of log10(eV)
	And your veff in units of cm^3 * steradian
	'''

	filename = sys.argv[1]
	data = np.genfromtxt(filename,delimiter=',',skip_header=1,names=['energy_logev','veff'])
	logeV = data['energy_logev']
	veff = data['veff']
	aeff = veff/tool.get_Lint(np.power(10.,logeV))

	flux_energy_logeV= np.arange(16,20,0.5)
	icecube_thrumu = flux.get_flux('icecube_thrumu',flux_energy_logeV)
	
	fig = plt.figure(figsize=(2.*11,8.5))
	ax_aeff = fig.add_subplot(1,2,1)
	ax_lim = fig.add_subplot(1,2,2)
	ax_aeff.plot(np.power(10.,logeV),aeff,'-o',linewidth=2.0,color='blue',label=r'Sample System')
	ax_lim.plot(np.power(10.,flux_energy_logeV),icecube_thrumu*np.power(10.,flux_energy_logeV),'-.', linewidth=3.0,color='orange',label=r'IceCube Thru-Mu (E$^{-2.19}$)')
	beautify_limit(ax_lim)
	beautify_aeff(ax_aeff)
	fig.savefig("test.png",edgecolor='none',bbox_inches="tight") #save the figure


def beautify_limit(this_ax):
	sizer=20
	xlow =  1.e15 #the lower x limit
	xup = 1e21 #the uppper x limit
	ylow = 1e-20 #the lower y limit
	yup = 1e-10 #the upper y limit
	this_ax.set_xlabel('Energy [eV]',size=sizer) #give it a title
	this_ax.set_ylabel('E F(E) [$cm^{-2} s^{-1} sr^{-1}$]',size=sizer)
	this_ax.set_yscale('log')
	this_ax.set_xscale('log')
	this_ax.tick_params(labelsize=sizer)
	this_ax.set_xlim([xlow,xup]) #set the x limits of the plot
	this_ax.set_ylim([ylow,yup]) #set the y limits of the plot
	this_legend = this_ax.legend(loc='upper right',title='Single Event Sensitivity')
	setp(this_legend.get_texts(), fontsize=17)
	setp(this_legend.get_title(), fontsize=17)
	this_ax.grid()

def beautify_aeff(this_ax):
	sizer=20
	xlow = 1.e15 #the lower x limit
	xup = 1.e21 #the uppper x limit
	ylow = 1.e2 #the lower x limit
	yup = 1.e10 #the uppper x limit
	this_ax.set_xlabel('Energy  [eV]',size=sizer) #give it a title
	this_ax.set_ylabel('[A$\Omega]_{eff}$  [cm$^2$sr]',size=sizer)
	this_ax.set_yscale('log')
	this_ax.set_xscale('log')
	this_ax.tick_params(labelsize=sizer)
	this_ax.set_xlim([xlow,xup]) #set the x limits of the plot
	this_ax.set_ylim([ylow,yup]) #set the y limits of the plot
	this_ax.grid()
	this_legend = this_ax.legend(loc='lower left',title='Effective Area')
	setp(this_legend.get_texts(), fontsize=17)
	setp(this_legend.get_title(), fontsize=17)


compute_counts()


