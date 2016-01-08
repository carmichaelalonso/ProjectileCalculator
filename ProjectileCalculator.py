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
from EquationSolver import sutat2, vuat, vuas, svut2

##
## Constants
##

g = -9.8	##gravity on earth (m/s^2)

def equationFinder(s, R, u, v, t, theta):

	## set theta to 0 if blank
	if theta is "":
		theta = 0


	##
	## Find values for empty variables
	## Sort through and find correct equation depending on variables available
	##

	##
	## height
	##
	if (s is ""):
		## find value of s

		if (v is not "") and (u is not "") and (t is not ""):
			## use svut2
			s = svut2(s, v, u, t, theta)

		elif (u is not "") and (v is not "") and (t is ""):
			## use vuas
			s = vuas(v, u, g, s, theta)

		elif (u is not "") and (t is not "") and (v is ""):
			## use sutat2
			s = sutat2(s, u, t, g, theta)

		else:
			## missing value, can't continue
			raise ValueError('Cannot calculate value for "s".')


	s = float(s)
	print ("Height (s -> m) is %d" % s)

	##
	## velocity
	##
	if (v is ""):
		## find value of v

		if (s is not "") and (u is not "") and (t is not ""):
			## use svut2
			v = svut2(s, v, u, t, theta)

		elif (u is not "") and (s is not "") and (t is ""):
			## use vuas
			v = vuas(v, u, g, s, theta)

		elif (u is not "") and (t is not "") and (s is ""):
			## use vuat
			v = vuat(v, u, g, theta)

		else:
			## missing value, can't continue
			raise ValueError('Cannot calculate value for "v".')

	v = float(v)
	print ("Velocity (v -> m/s) is %d" % v)

	##
	## initial velocity
	##
	if (u is ""):
		## find value of u

		if (s is not "") and (v is not "") and (t is not ""):
			## use svut2
			u = svut2(s, v, u, t, theta)

		elif (v is not "") and (s is not "") and (t is ""):
			## use vuas
			u = vuas(v, u, g, s, theta)

		elif (v is not "") and (t is not "") and (s is ""):
			## use vuat
			u = vuat(v, u, g, theta)

		elif (s is not "") and (t is not "") and (v is ""):
			## use sutat2
			u = sutat2(s, u, t, g, theta)

		else:
			## missing value, can't continue
			raise ValueError('Cannot calculate value for "u".')

	u = float(u)
	print ("Initial velocity (u -> m/s) is %d" % u)

	##
	## time
	##
	if (t is ""):
		## find value of t

		if (s is not "") and (v is not "") and (u is not ""):
			## use svut2
			t = svut2(s, v, u, t, theta)

		elif (v is not "") and (u is not "") and (s is ""):
			## use vuat
			t = vuat(v, u, g, theta)

		elif (s is not "") and (u is not "") and (v is ""):
			## use sutat2
			t = sutat2(s, u, t, g, theta)

		else:
			## missing value, can't continue
			raise ValueError('Cannot calculate value for "t".')

	t = float(t)
	print ("Time (t -> s) is %d" % t)

	
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

	print "\nSolving...\n\n"

	equationFinder(s, R, u, v, t, theta)
