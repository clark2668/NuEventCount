# -*- coding: utf-8 -*-
import numpy as np #import numpy
import math
import constants as const

def get_Lint(energy_eV, which_sigma=None):
	"""
	get_Lint

	This is a parameterization of the neutrino effective length.
	By default, it will use a cross section 
	measurement from Ghandi et. al. (10.1103/PhysRevD.58.093009)


	Parameters
	----------
	logev (float): energy in eV
		energy of your neutrino in electron volts

	Returns
	-------
	Lint (float): interaction length
		interaction length of a neutrino in centimeters
	"""
	Lint=0.

	if(which_sigma==None):
		#by default, assuem Ghandi et. al. (10.1103/PhysRevD.58.093009)

		sigma = 7.84e-36 * ((energy_eV/1.e9)**0.363)
		Lint = const.NucleonMass / (const.EarthDensity * sigma)

	return Lint


def get_flux(resource_name, energy_vals_logeV):
	"""
	get_flux

	Return the flux of neutrinos as a function of energy


	Parameters
	----------
	resource_name: name of the flux you want
		name of the flux you want
	energy_vals_logeV:
		the energies you want the flux evaluted at, in units of log10(eV)

	Returns
	-------
	flux: ndarray
		the flux prediction in units of 1/cm^2/s/sr

	"""
	flux = np.array([])

	if(resource_name=='icecube_thrumu'):
		def icecube_thrumu_function(E):
			return 3.03 * ((E/1.e14)**-2.19) * 1e-27
		flux = icecube_thrumu_function(np.power(10.,energy_vals_logeV))

	elif(resource_name=='icecube_combined'):
		def icecube_combined_function(E):
			return 6.7 * ((E/1.e14)**-2.50) * 1e-27
		flux = icecube_combined_function(np.power(10.,energy_vals_logeV))

	return flux