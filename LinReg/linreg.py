import numpy as np 
import matplotlib.pyplot as plt 
from numpy import genfromtxt


def estimate_coef(x, y): 
	# number of observations/points 
	n = np.size(x) 

	# mean of x and y vector 
	m_x, m_y = np.mean(x), np.mean(y) 
	print("MEAN X", m_x)
	print("MEAN Y", m_y)

	# calculating cross-deviation and deviation about x 
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 

	print("SSXY", SS_xy)
	print("SS X", SS_xx)


	# calculating regression coefficients 
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x 

	return(b_0, b_1) 

def plot_regression_line(x, y, b): 
	# plotting the actual points as scatter plot 
	plt.scatter(x, y, color = "m", 
			marker = "o", s = 30) 

	# predicted response vector 
	y_pred = b[0] + b[1]*x 

	# plotting the regression line 
	plt.plot(x, y_pred, color = "g") 

	# putting labels 
	plt.xlabel('x') 
	plt.ylabel('y') 

	# function to show plot 
	plt.show() 

def main(): 
	data = genfromtxt('./testr.csv', delimiter=',')
	x=np.zeros(8)
	y=np.zeros(8)

	# observations 
	for i in range(8):
		x[i]=np.array(data[i][0])
		y[i]=np.array(data[i][1])

	#x = np.array([10,20,30,40,50,60,70,80,90,100]) 
	#y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
	#print(x)


	# estimating coefficients 
	b = estimate_coef(x, y) 
	print("Estimated coefficients:\nb_0 = {}\nb_1 = {}".format(b[0], b[1]))
	
	#TRAINING ERROR
	sum=0
	for i in range(8):
		factor= y[i] - b[0] - b[1]*x[i]
		sum= sum + factor*factor
	train_error= sum/8

	print("Training error= {}", train_error)


	#TESTING ERROR
	test_data = genfromtxt('./testr.csv', delimiter=',')
	x=np.zeros(8)
	y=np.zeros(8)

	# observations 
	for i in range(8):
		x[i]=np.array(data[i][0])
		y[i]=np.array(data[i][1])
	sum=0
	for i in range(8):
		factor= y[i] - b[0] - b[1]*x[i]
		sum= sum + factor*factor
	test_error= sum/8

	print("Testing error= {}", test_error)

	# plotting regression line 
	plot_regression_line(x, y, b) 


if __name__ == "__main__": 
	main() 

























