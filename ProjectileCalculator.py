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

g = 9.8	##gravity on earth (m/s^2)

def simulate(s, R, u, v, t, theta):

	## set theta to 0 if blank
	if theta is "":
		theta = 0


	##
	## Find values for empty variables
	## Sort through and find correct equation depending on variables available
	##




##
## time
##
def findTime(s, u, v, theta):
	if (t is ""):
		## find value of t

		if (s is not "") and (v is not "") and (u is not ""):
			## use svut2
			tVal = svut2(s, v, u, t, theta)

		elif (v is not "") and (u is not "") and (s is ""):
			## use vuat
			tVal = vuat(v, u, g, t, theta)

		elif (s is not "") and (u is not "") and (v is ""):
			## use sutat2
			tVal = sutat2(s, u, t, g, theta)

		else:
			## missing value, can't continue
			raise ValueError('Cannot calculate value for "t".')

		tVal = float(tVal)

	else:
		tVal = float(t)

	
	print ("Time (t -> s) is %d" % tVal)
	return tVal

##
## height
##
def findHeight(u, v, t, theta):
	if (s is ""):
		## find value of s

		if (v is not "") and (u is not "") and (t is not ""):
			## use svut2
			sVal = svut2(s, v, u, t, theta)

		elif (u is not "") and (v is not "") and (t is ""):
			## use vuas
			sVal = vuas(v, u, g, s, theta)

		elif (u is not "") and (t is not "") and (v is ""):
			## use sutat2
			sVal = sutat2(s, u, t, g, theta)

		else:
			## missing value, can't continue
			raise ValueError('Cannot calculate value for "s".')

		sVal = float(sVal)

	else:
		sVal = float(sVal)

	print ("Height (s -> m) is %d" % sVal)
	return sVal

##
## velocity
##
def findVelocity(s, u, t, theta):
	if (v is ""):
		## find value of v

		if (s is not "") and (u is not "") and (t is not ""):
			## use svut2
			vVal = svut2(s, v, u, t, theta)

		elif (u is not "") and (s is not "") and (t is ""):
			## use vuas
			vVal = vuas(v, u, g, s, theta)

		elif (u is not "") and (t is not "") and (s is ""):
			## use vuat
			vVal = vuat(v, u, g, t, theta)

		else:
			## missing value, can't continue
			raise ValueError('Cannot calculate value for "v".')

		vVal = float(vVal)

	else:
		vVal = float(v)

	print ("Velocity (v -> m/s) is %d" % vVal)
	return vVal
	

##
## initial velocity
##
def findInitialVelocity(s, v, t, theta):
	if (u is ""):
		## find value of u

		if (s is not "") and (v is not "") and (t is not ""):
			## use svut2
			uVal = svut2(s, v, u, t, theta)

		elif (v is not "") and (s is not "") and (t is ""):
			## use vuas
			uVal = vuas(v, u, g, s, theta)

		elif (v is not "") and (t is not "") and (s is ""):
			## use vuat
			uVal = vuat(v, u, g, t, theta)

		elif (s is not "") and (t is not "") and (v is ""):
			## use sutat2
			uVal = sutat2(s, u, t, g, theta)

		else:
			## missing value, can't continue
			raise ValueError('Cannot calculate value for "u".')

		uVal = float(uVal)

	else:
		uVal = float(u)

	print ("Initial velocity (u -> m/s) is %d" % uVal)
	return uVal

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

	simulate(s, R, u, v, t, theta)
