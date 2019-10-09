# NAIVE BAYES CLASSIFIER
# Built by MUNEEB AHMED, M.TECH CSE, JAMIA MILLIA ISLAMIA


import numpy as np



def P_Conditional(var_no, wrt_var_no,value, value2, X_Y):
	#P(A given B) = P(A intersect B)/ P(B)
	count1=0
	count2=0
	totalcount=0
	laplace_A=0.001
	m,n= X_Y.shape
	for i in range(m):
		for j in range(n):
			if j==var_no-1:
				if X_Y[i,j]==value:
					if X_Y[i,wrt_var_no-1]==value2:
						count1=count1+1
	count1=count1+laplace_A

	for i in range(m):
		for j in range(n):
			if j==wrt_var_no-1:
				if X_Y[i,j]==value2:
					count2=count2+1
	count2=count2+laplace_A

	#print(count, totalcount)
	return (count1/count2)

def P_Unconditional(var_no, value, X_Y):
	
	count=0
	totalcount=0
	laplace_A=0.001
	m,n= X_Y.shape
	for i in range(m):
		for j in range(n):
			if j==var_no-1:
				if X_Y[i,j]==value:
					count=count+1
	count=count+laplace_A
	totalcount=m+laplace_A
	#print(count, totalcount)
	return (count/totalcount)
def main():
	


	#get training data
	heading=np.array(["X1","X2","Label"]);	
	X_Y= np.array([[0, 1, 1],
				[0, 0, 0],
				[1, 0, 1]])
	LABEL=np.array([0,1])
    	
	print(heading)
	print(X_Y)
	m,n= X_Y.shape
	

	#fitting
	#It means what is the probabilty of 3rd varaible to get value 0
	P_Y_0=P_Unconditional(3,0,X_Y)
	#print(P_Y_0)
	P_Y_1=P_Unconditional(3,1,X_Y)
	#print(P_Y_1)
	#3rd variable is our LABEL i.e., Y_output
	#3rd variable is our LABEL i.e., Y_output
	

	#P_X2_0_Y_1= P_Conditional(2,3,0, 1, X_Y)
	#print('x2Y1:',P_X2_0_Y_1)
	
	#TESTING

	testdata_X=np.array([0,1])
	N=testdata_X.shape
	#for LBL in LABEL:
	#	for j in testdata_X:
	#		P
	

	#last but one variable beacuse that represents Y_output
	P_Y0 = P_Conditional(1,3,1,0,X_Y)* P_Conditional(2,3,1,0,X_Y)  
	P_Y0=P_Y0*P_Unconditional(3,0,X_Y)

	P_Y1 = P_Conditional(1,3,1,1,X_Y)* P_Conditional(2,3,1,1,X_Y)  
	P_Y1=P_Y1*P_Unconditional(3,1,X_Y)

	print('Probabilty Y=0:', P_Y0)
	print('Probabilty Y=1:', P_Y1)


if __name__ == "__main__":
	main()


