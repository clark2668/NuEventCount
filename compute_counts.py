# -*- coding: utf-8 -*-
import numpy as np
import sys
import constants as const

def compute_counts():

	filename = sys.argv[1]
	print filename
	data = np.genfromtxt(filename,delimiter=',',skip_header=1,names=['energy_logev','veff'])
	veff=data['veff']
	print veff
	# energy = np.array([17.,17.5,18.,18.5,19.,19.5,20.,20.5,21.])

compute_counts()