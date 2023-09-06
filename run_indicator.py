#
# Author: Diana Valencia
# Description: This code implements the ILAP indicator presented in the following article:
# Valencia-Rodríguez, D.C., Coello Coello, C.A. (2023). A Novel Performance Indicator Based on the Linear Assignment 
# Problem. In: Emmerich, M., et al. Evolutionary Multi-Criterion Optimization. EMO 2023. Lecture Notes in Computer 
# Science, vol 13970. Springer, Cham. https://doi.org/10.1007/978-3-031-27250-9_25
#


import sys
import numpy as np
from scipy.optimize import linear_sum_assignment

#
# Description: Verify if a number is float 
# Parameters: A number (n)
#
def is_float(n):
	try:
		float(n)
		return True
	except:
		return False


#
# Description: Reads the points in the given file
# Parameters: File name (fileName)
#

def getPointsFromFile(fileName):
	try:
		file=open(fileName,"r")
		lines = file.readlines()
		file.close()
	except IOError:
		print("ERROR: Can not open the file: ",fileName)
		sys.exit()

	points = []
	for line in lines:
		if line[0] != "#":
			point = []
			for n in line.split():
				if is_float(n) :
					point.append(float(n))
				else : 
					print("ERROR: Wrong format in ",fileName)
					sys.exit()
			points.append(point)
	obj_size = len(points[0])
	for pt in points:
		if len(pt) != obj_size:
			print("ERROR: Wrong dimension in ", fileName)
			sys.exit()
	return points

#
# Description: Evaluates the achievement scalarizing function
# Parameters: The objective values (f) and a weight vector (w)
#

def ASF( f, w ):
	vmax = 0
	wzero = 1e-2
	if len(f) == 2:
		wzero = 1e-6
	for fi,wi in zip(f,w):
		if abs(wi) < wzero: 
			wi = wzero
		v = fi/wi
		if( v > vmax ):
			vmax = v
	return vmax

#
# Description: Computes the cost matrix of the linear assignment problem
# Parameters: The set of uniformly distributed weight vectors (weights) and
# 			  the Pareto front approximation to evaluate (points)
#	

def compute_cost(weights, points):
	cost_matrix = []
	for w in weights:
		cost_row = []
		for pt in points:
			cost_row.append( ASF(pt, w ) )
		cost_matrix.append(cost_row)
	return np.array(cost_matrix)

#
# Description: Computes ILAP indicator
# Parameters: the set of uniformly distributed weight vectors (weights) and
# 			  the Pareto front approximation to evaluate (points)
#
def compute_LAP_indicator(weights, points):
	cost_matrix = compute_cost(weights, points)
	row_ind, col_ind = linear_sum_assignment(cost_matrix)
	return cost_matrix[row_ind, col_ind].sum()/len(points)

def main():
	n = len(sys.argv)
	if n != 3:
		print("python3 run_indicator.py weights_file points_file")
		exit(-1)

	w_file = sys.argv[1]
	p_file = sys.argv[2]

	weights = getPointsFromFile(w_file)
	points = getPointsFromFile(p_file)
	
	if( len(weights) != len(points) ) or ( len(weights[0]) != len(points[0]) ):
		print("ERROR: weights and points dimension does not match!")
		exit(-1)

	ind = compute_LAP_indicator(weights, points)
	print("LAP_indicator: "+ str(ind))

main()