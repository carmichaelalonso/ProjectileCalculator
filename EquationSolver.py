"""

EquationSolver.py
Copyright Cameron Carmichael Alonso, 2016. All Rights Reserved.

"""

from mpmath import *

def sutat2(u, t, a):
	## performs equation s = u t + 1/2 a t^2
	
	uFloat = float(u)
	tFloat = float(t)
	aFloat = float(a)

	s = ((uFloat*tFloat) + power((0.5)*aFloat*tFloat, 2))
	return s