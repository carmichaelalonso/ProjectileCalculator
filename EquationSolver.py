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

		## blank line to keep tidy
		print "\n\n"

	return result

def vuat(vVal, uVal, aVal, tVal):
	## performs equation v = u + at
	print "\nSolving using v = u + a t"

	## define symbols for equation
	v, u, a, t = symbols('v u a t')

	##
	## try and convert values to float
	## when exception is found, keep string blank
	##
	try:
		vFloat = float(vVal)
	except:
		vVal = ""

	try:
		uFloat = float(uVal)
	except:
		uVal = ""

	try:
		aFloat = float(aVal)
	except:
		aVal = ""

	try:
		tFloat = float(tVal)
	except:
		tVal = ""

	##
	## check which value is to be solved
	##
	if vVal is "":
		## solve for v and substitute
		print "Solving for v..."

		equation = solve((-v+u+a*t).subs([(u, uFloat), (t, tFloat), (a, aFloat)]), v)
		result = equation[0]
		print result

	elif uVal is "":
		## solve for u and substitute
		print "Solving for u..."

		equation = solve((-v+u+a*t).subs([(t, tFloat), (v, vFloat), (a, aFloat)]), u)
		result = equation[0]
		print result

	elif aVal is "":
		## solve for a and substitute
		print "Solving for a..."

		equation = solve((-v+u+a*t).subs([(v, vFloat), (u, uFloat), (t, tFloat)]), a)
		result = equation[0]
		print result

	elif tVal is "":
		## solve for t and substitute
		print "Solving for t..."

		equation = solve((-v+u+a*t).subs([(v, vFloat), (u, uFloat), (a, aFloat)]), t)
		result = equation[0]
		print result

		## blank line to keep tidy
		print "\n\n"
		
	return result


def vuas(vVal, uVal, aVal, sVal):
	## performs equation v^2 = u^2 + 2as
	print "\nSolving using v^2 = u^2 + 2as"

	## define symbols for equation
	v, u, a, s = symbols('v u a s')

	##
	## try and convert values to float
	## when exception is found, keep string blank
	##
	try:
		vFloat = float(vVal)
	except:
		vVal = ""

	try:
		uFloat = float(uVal)
	except:
		uVal = ""

	try:
		aFloat = float(aVal)
	except:
		aVal = ""

	try:
		sFloat = float(sVal)
	except:
		sVal = ""

	##
	## check which value is to be solved
	##
	if vVal is "":
		## solve for v and substitute
		print "Solving for v..."

		equation = solve((-v**2+u**2+2*a*s).subs([(u, uFloat), (s, sFloat), (a, aFloat)]), v)
		result = equation[0]
		print result

	elif uVal is "":
		## solve for u and substitute
		print "Solving for u..."

		equation = solve((-v**2+u**2+2*a*s).subs([(v, vFloat), (a, aFloat), (s, sFloat)]), u)
		result = equation[0]
		print result

	elif aVal is "":
		## solve for a and substitute
		print "Solving for a..."

		equation = solve((-v**2+u**2+2*a*s).subs([(v, vFloat), (u, uFloat), (s, sFloat)]), a)
		result = equation[0]
		print result

	elif sVal is "":
		## solve for s and substitute
		print "Solving for s..."

		equation = solve((-v**2+u**2+2*a*s).subs([(v, vFloat), (u, uFloat), (a, aFloat)]), s)
		result = equation[0]
		print result

		## blank line to keep tidy
		print "\n\n"
		
	return result

def svut2(sVal, vVal, uVal, tVal):
	## performs equation s = ((v+u)*t)/2
	print "\nSolving using s = ((v+u)*t)/2"

	## define symbols for equation
	s, v, u, t = symbols('s v u t')

	##
	## try and convert values to float
	## when exception is found, keep string blank
	##
	try:
		sFloat = float(sVal)
	except:
		sVal = ""

	try:
		vFloat = float(vVal)
	except:
		vVal = ""

	try:
		uFloat = float(uVal)
	except:
		uVal = ""

	try:
		tFloat = float(tVal)
	except:
		tVal = ""

	##
	## check which value is to be solved
	##
	if sVal is "":
		## solve for s and substitute
		print "Solving for s..."

		equation = solve(((-s*(v+u)*t)/2).subs([(v, vFloat), (u, uFloat), (t, tFloat)]), s)
		result = equation[0]
		print result

	elif vVal is "":
		## solve for v and substitute
		print "Solving for v..."

		equation = solve(((-s*(v+u)*t)/2).subs([(s, sFloat), (u, uFloat), (t, tFloat)]), v)
		result = equation[0]
		print result

	elif uVal is "":
		## solve for u and substitute
		print "Solving for u..."

		equation = solve(((-s*(v+u)*t)/2).subs([(s, sFloat), (v, vFloat), (t, tFloat)]), u)
		result = equation[0]
		print result

	elif tVal is "":
		## solve for t and substitute
		print "Solving for t..."

		equation = solve(((-s*(v+u)*t)/2).subs([(s, sFloat), (v, vFloat), (u, uFloat)]), t)
		result = equation[0]
		print result

		## blank line to keep tidy
		print "\n\n"
		
	return result