"""

ProjectileCalculator.py
Copyright Cameron Carmichael Alonso, 2016. All Rights Reserved.

"""

import sys
from EquationSolver import sutat2

##
## Variables:
## s - distance (x, y); R refers to s.x
## u - initial velocity (x, y; optional sin() or cos() component)
## v - velocity (x, y; optional sin() or cos() component)
## a - acceleration (x, y)
## t - time
##
##
## We need to find:
##  - s
##  - t
##

def equationFinder(s, R, u, v, a, t, theta):

	## set theta to 45 if blank
	if theta is "":
		theta = 45

	if s is "":
		## we need to calculate s

		if (u is not "") and (t is not "") and (a is not ""):
			# we can use the s = u t + 1/2 a t^2 equation
			s = sutat2(u, t, a)

	

##
## Entry point
##
if __name__ == "__main__":

	print "\n\nEnter variables below. Keep blank if no value is to be specifed."

	## get variables
	s = raw_input("s (m) = ")
	R = raw_input("R (m) = ")
	u = raw_input("u (m/s) = ")
	v = raw_input("v (m/s) = ")
	a = raw_input("a (m/s^2) = ")
	t = raw_input("t (s) = ")
	theta = raw_input("Theta = ")

	equationFinder(s, R, u, v, a, t, theta)

	


