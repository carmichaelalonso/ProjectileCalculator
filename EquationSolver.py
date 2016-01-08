"""

EquationSolver.py
Copyright Cameron Carmichael Alonso, 2016. All Rights Reserved.

"""

from mpmath import *
from sympy import *

def sutat2(sVal, uVal, tVal, aVal):
	## performs equation s = u t + 1/2 a t^2
	print "\nSolving using s = u t + 1/2 a t^2"

	## define symbols for equation
	s, u, t, a = symbols('s u t a')

	##
	## try and convert values to float
	## when exception is found, keep string blank
	##
	try:
		sFloat = float(sVal)
	except:
		sVal = ""

	try:
		uFloat = float(uVal)
	except:
		uVal = ""

	try:
		tFloat = float(tVal)
	except:
		tVal = ""

	try:
		aFloat = float(aVal)
	except:
		aVal = ""


	##
	## check which value is to be solved
	##
	if sVal is "":
		## solve for s and substitute
		print "Solving for s..."

		equation = solve((-s+(u*t)+(0.5)*a*t**2).subs([(t, tFloat), (u, uFloat), (a, aFloat)]), s)
		result = equation[0]
		print result

	elif uVal is "":
		## solve for u and substitute
		print "Solving for u..."

		equation = solve((-s+(u*t)+(0.5)*a*t**2).subs([(t, tFloat), (s, sFloat), (a, aFloat)]), u)
		result = equation[0]
		print result

	elif tVal is "":
		## solve for t and substitute
		print "Solving for t..."

		equation = solve((-s+(u*t)+(0.5)*a*t**2).subs([(s, tFloat), (u, uFloat), (a, aFloat)]), t)
		result = equation[0]
		print result

	elif aVal is "":
		## solve for a and substitute
		print "Solving for a..."

		equation = solve((-s+(u*t)+(0.5)*a*t**2).subs([(s, tFloat), (u, uFloat), (t, tFloat)]), a)
		result = equation[0]
		print result

	return result
