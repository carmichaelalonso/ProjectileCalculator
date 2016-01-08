"""

ProjectileCalculator.py
Copyright Cameron Carmichael Alonso, 2016. All Rights Reserved.

"""

##
## Variables:
## s - distance (x, y); R refers to s.x
## u - initial velocity (x, y; optional sin() or cos() component)
## v - velocity (x, y; optional sin() or cos() component)
## t - time
##

import sys
from EquationSolver import sutat2

##
## Constants
##
g = -9.8	## gravity on earth (m/s^2)

def equationFinder(s, R, u, v, t, theta):

	## set theta to 0 if blank
	if theta is "":
		theta = 0

	if (u is not "") and (t is not "") and (a is not "") and (s is ""):
		## we have u, a and t -> solve for s
		## we can use the s = u t + 1/2 a t^2 equation
		s = sutat2(s, u, t, g, theta)

	
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
	t = raw_input("t (s) = ")
	theta = raw_input("Theta (from x-axis) = ")

	equationFinder(s, R, u, v, t, theta)
