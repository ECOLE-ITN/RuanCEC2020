import os
import numpy as np

from decimal import *
getcontext().prec=4

# DMOP = ['FDA4', 'FDA5', 'FDA5_iso', 'FDA5_dec', 'DIMP2', 'dMOP2','dMOP2_iso', 'dMOP2_dec', 'dMOP3', 'HE2', 'HE7', 'HE9']
DMOP = ['FDA4']
Copyfilepath = 'Tr-DMOEA(CEC)Test/active-TR-DMOEA/Tr-RMMEDA/Results/'

group = [5,6]

for i in range(len(DMOP)):
	for j in group:
		IGDCopy = []
		for run in range(1,21):
			CopyIGD = []
			CopyIGDFilePath = Copyfilepath +  'run' + str(run) + '\\IGD-AfTr\\' + DMOP[i] + '\\group' + str(j)
			CopyrIGDFileName = CopyIGDFilePath +  '\\IGD_AfTr.txt'

			with open(CopyrIGDFileName, 'r') as f:
				line = f.readline()
				CopyIGD = line.split()
			CopyIGD = np.mean(list(map(float,CopyIGD)))
			IGDCopy.append(CopyIGD)
		print(IGDCopy)