
# coding: utf-8

# In[3]:

# NAIVE BAYES CLASSIFIER
# Built by MUNEEB AHMED, M.TECH CSE, JAMIA MILLIA ISLAMIA


import numpy as np
import pandas as pd


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
	heading=np.array(["X1","X2","X3","X4","Y_output"])
	heading=np.array(['Outlook','Temperature','Humidity','Windy','Play golf'])
	X_Y= np.array(
[['Sunny','Hot','High','FALSE','No'],
['Sunny','Hot','High','TRUE','No'],
['Overcast','Hot','High','FALSE','Yes'],
['Rainy','Mild','High','FALSE','Yes'],
['Rainy','Cool','Normal','FALSE','Yes'],
['Rainy','Cool','Normal','TRUE','No'],
['Overcast','Cool','Normal','TRUE','Yes'],
['Sunny','Mild','High','FALSE','No'],
['Sunny','Cool','Normal','FALSE','Yes'],
['Rainy','Mild','Normal','FALSE','Yes'],
['Sunny','Mild','Normal','TRUE','Yes'],
['Overcast','Mild','High','TRUE','Yes'],
['Overcast','Hot','Normal','FALSE','Yes'],
['Rainy','Mild','High','TRUE','No']]
)
    
    
    
	#data= pd.read_csv("C:\\Users\\M Tech Lab\\Desktop\\naive.csv")
	#var=pd.DataFrame(data)   
	#X1=var["Outlook"].tolist()
	#print(X1)

	print(heading)
	print(X_Y)
	m,n= X_Y.shape
	

	#fitting
	#It means what is the probabilty of 3rd varaible to get value 0
	#P_Y_0=P_Unconditional(3,0,X_Y)
	#print('Probabilty (Y=0): ',P_Y_0)
	#P_Y_1=P_Unconditional(3,1,X_Y)
	#print('Probabilty (Y=1): ',P_Y_1)
	
    
    
    #3RD VARIABLE is Y, X2 is var_no=2, X1 is var_no=1
	#P_X1_1_given_Y_1 = P_Conditional(1,3,1,1,X_Y)
	#print('\n\n\nProbabilty (X1=1|Y=1): ',P_X1_1_given_Y_1)
	    
	#P_X2_0_given_Y_0 = P_Conditional(1,3,0,0,X_Y)
	#print('Probabilty (X2=1|Y=1): ',P_X2_0_given_Y_0 )
	#3rd variable is our LABEL i.e., Y_output
	#3rd variable is our LABEL i.e., Y_output
	

	#P_X2_0_Y_1= P_Conditional(2,3,0, 1, X_Y)
	#print('x2Y1:',P_X2_0_Y_1)
	
	#TESTING


	#for LBL in LABEL:
	#	for j in testdata_X:

	X_test=np.array(['Sunny','Cool','Normal','FALSE'])
	Y_test=np.array(['No','Yes'])    
	#print(X[0])
    
    #ALLCOMBINATIONS
	x1=np.array(['Sunny','Outlook','Rainy'])
	x2=np.array(['Hot','Mild','Cold'])    
	x3=np.array(['High','Normal'])    
	x4=np.array(['Yes','No'])

    
	for i in x1:
		for j in x2:
			for k in x3:
				for l in x4:
					X_test=np.array([i,j,k,l])
					print ('\n',X_test)
					#last but one variable beacuse that represents Y_output
					P_Y0 = P_Conditional(1,5,X_test[0], Y_test[0],X_Y) * P_Conditional(2,5,X_test[1],Y_test[0],X_Y) * P_Conditional(3,5,X_test[2],Y_test[0],X_Y) * P_Conditional(4,5,X_test[3],Y_test[0],X_Y)
					P_Y0=P_Y0*P_Unconditional(5,Y_test[0],X_Y)

					P_Y1 = P_Conditional(1,5, X_test[0], Y_test[1],X_Y) * P_Conditional(2,5,X_test[1],Y_test[1],X_Y) * P_Conditional(3,5,X_test[2],Y_test[1],X_Y) * P_Conditional(4,5,X_test[3],Y_test[1],X_Y)
					P_Y1=P_Y1*P_Unconditional(5,Y_test[1],X_Y)

					print('\n\nProbabilty Play=NO:', P_Y0)
					print('Probabilty Play=YES:', P_Y1)
    





if __name__ == "__main__":
	main()




# In[ ]:



