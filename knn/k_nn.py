import numpy as np
import math
import matplotlib.pyplot as plt 

def plotit(dataset,testdata,mycolor):
	x=np.zeros(500)
	y=np.zeros(500)
	c=np.zeros(500)
	for i in range(500):
		x[i]=dataset[i][0]
		y[i]=dataset[i][1]
		c[i]=dataset[i][2]
		if(c[i]==1):
			plt.scatter(x[i], y[i], color = "m", 
			marker = "o", s = 10)
		else:
			plt.scatter(x[i], y[i], color = "g", 
			marker = "o", s = 10)
		
	plt.xlabel('x') 
	plt.ylabel('y') 

	# function to show plot

	plt.scatter(testdata[0], testdata[1], color = mycolor, marker = "o", s = 20)
	

	plt.show() 

def distance(a1,a2):
	#np.sqr(a1-a2)
	return pow(a1-a2,2)

def Citydistance(a1,a2):
	#np.sqr(a1-a2)
	return abs(a1-a2)

def sort(k,myarray):
	#m,n=myarray.shape
	#for i in range(m):
	#	for j in range(n)
	return
def main():
	
	
	#dataset= np.list([[2,3,'A'],[4,5,'B']])
	dataset=np.zeros(shape=(500,3))
	
	dataset = np.genfromtxt('./foo.csv', delimiter=',')
	

	print(dataset)
	testdata = np.array([260,60])

	plotit(dataset,testdata,"b")


	myarray= np.zeros(shape=(500,2))
	
	sum=0;

	
	
	m,n= dataset.shape

	for i in range(m):
		sum=0 
		for j in range (n-1):
			sum +=distance(testdata[j],dataset[i][j])
		res=math.sqrt(sum)
		myarray[i][0]=res
		myarray[i][1]=dataset[i][2] 

	
	print("\n\n\n\n\n\n", myarray)

	print("Enter value of K:")
	k=input()

	#sort myarray
	myarray=np.sort(myarray,axis=0)
	print("Array after sorting in Desc:\n",myarray)
	#display top k elements
	
	print("Top k=%d elements are: \n",k)
	for i in range(int(k)):
		print("\n", myarray[i])

	#display the orresponding class using majority voting
	#there can be n-classes, which i take statically here
	#although can be done in initail read of the dataset
	c1=c2=0
	for i in range(int(k)):
			if(myarray[i][1]==1):	#classno=1
				c1=c1+1
			if(myarray[i][1]==2):	#classno=1
				c2=c2+1

	if(c1>=c2):
		mycolor="m"
	else:
		mycolor="g"

	plotit(dataset,testdata,mycolor)

if __name__ =='__main__':
	main()