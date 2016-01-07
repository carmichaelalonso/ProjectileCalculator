"""

EquationSolver.py
Copyright Cameron Carmichael Alonso, 2016. All Rights Reserved.

"""

from mpmath import *
from sympy import *

def sutat2(sVal, uVal, tVal, aVal):
	## performs equation s = u t + 1/2 a t^2
	
	## define symbols for equation
	s, u, t, a = symbols('s u t a')


	if (sVal is ""):
		## solve for s

		## convert necessary values to float
		uFloat = float(uVal)
		tFloat = float(tVal)
		aFloat = float(aVal)

		## solve for s and substitute
		equation = solve((-s+(u*t)+(0.5)*a*t**2), s)
		equation = equation[0]
		equation.subs([(t, tFloat), (u, uFloat), (u, uFloat)])
		print equation

	#s = ((uFloat*tFloat) + power((0.5)*aFloat*tFloat, 2))
	return 22

def rearrange():
	s, u, t, a = symbols('s u t a')

	r = solve((-s+(u*t)+(0.5)*a*t**2), s)
	print r