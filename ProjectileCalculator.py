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
from Interface import PlotGraph

##
## Constants
##

g = 9.8	## gravity on earth (m/s^2)
tDenomenator = 100 ## how many times to divide (t) by

def simulate(s, R, u, v, t, theta):

	## set (theta) to 0 if blank
	if theta is "":
		theta = 0



	##
	## Check to see if we have a (t) value
	##

	tVal = findTime(t, s, u, v, theta)
	t = str(tVal)

	##
	## Divide time by tDenomenator
	##

	tDelta = (tVal / tDenomenator)
	print ("Time delta is %.5f\n\n" % tDelta)

	xValues = []
	yValues = []

	## loop through adding tDelta each time
	for i in range(0,tDenomenator):
		currentT = (tDelta * i)
		xValues.append(currentT)

		##
		## For each time, find corresponding (s)
		## This is where (v) = "" (no need to calc (v) just yet)
		##
		sVal = findHeight(s, u, "", currentT, theta)
		yValues.append(sVal)

		print ("%.3f, %.3f" % (currentT, sVal))


	labelString = ("s = %s; u = %s; v = %s; t = %s; theta = %s" % (s, u, v, t, theta))
	PlotGraph(xValues, yValues, labelString)

##
## time
##
def findTime(t, s, u, v, theta):
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

	else:
		tVal = float(t)

	
	print ("Time (t -> s) is %.10f" % tVal)
	return tVal

##
## height
##
def findHeight(s, u, v, t, theta):
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
		sVal = float(s)

	print ("Height (s -> m) is %.10f" % sVal)
	return sVal

##
## velocity
##
def findVelocity(v, s, u, t, theta):
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

	print ("Velocity (v -> m/s) is %.10f" % vVal)
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

	print ("Initial velocity (u -> m/s) is %.10f" % uVal)
	return uVal

##
## Entry point
##
if __name__ == "__main__":

	print "\n\nEnter variables below. Keep blank if no value is to be specifed."

	## get variables
	s = raw_input("s (m) = ")
	R = 0 ##R = raw_input("R (m) = ")
	u = raw_input("u (m/s) = ")
	v = raw_input("v (m/s) = ")
	t = raw_input("t (s) = ")
	theta = raw_input("Theta (from x-axis) = ")

	print "\nSolving...\n\n"

	simulate(s, R, u, v, t, theta)
