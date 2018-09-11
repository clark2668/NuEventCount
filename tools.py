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