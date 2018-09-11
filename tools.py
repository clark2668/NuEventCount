# -*- coding: utf-8 -*-
import numpy as np #import numpy
import math
import constants as const

def get_Lint(energy_eV):
	"""
	get_Lint

	Parameters
	----------
	logev (float): energy in eV
		energy of your neutrino in electron volts

	Returns
	-------
	Lint (float): interaction length
		interaction length of a neutrino in centimeters
	"""