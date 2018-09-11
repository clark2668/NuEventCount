# -*- coding: utf-8 -*-
import numpy as np #import numpy
import math

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
	energy_bins: ndarray
		the energy bins the limit is defined over in the units of log10(eV)
	flux_prediction: ndarray
		the flux prediction in units of 1/cm^2/s/sr

	"""
	flux = np.array([])

	if(resource_name=='icecube_thrumu'):
		def icecube_thrumu_function(E):
			return 3.03 * ((E/1.e14)**-2.19) * 1e-27
		flux = icecube_thrumu_function(np.power(10.,energy_vals_logeV))

	else if(resource_name=='icecube_combined'):
		def icecube_combined_function(E):
			return 6.7 * ((E/1.e14)**-2.50) * 1e-27
		flux = icecube_combined_function(np.power(10.,energy_vals_logeV))

	return flux