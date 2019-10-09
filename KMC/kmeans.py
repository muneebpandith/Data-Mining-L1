import numpy as np
import math
import matplotlib.pyplot as plt
import random as random

count=0;

def getInitialMean(MEAN):
	k,n=MEAN.shape

	for i in range(k):
		for j in range(n):
			MEAN[i][j]=np.random.rand()*12  #*12 is just Muneebs goodlooking factor
	#MEAN=np.array([[ 5.60129388,9.44370942],[ 9.6005662,6.26615678]])

	return MEAN

def updateMean(dataset,MEAN):
	k,n=MEAN.shape
	rows,cols=dataset.shape


	COUNT=np.zeros(shape=(n,k))
	SUM=np.zeros(shape=(n,k))

	SUM0x=SUM0y=SUM1x=SUM1y=1
	COUNT0x=COUNT0y=COUNT1x=COUNT1y=1
	
	for i in range(rows-1):
		for j in range(cols-1):

			'''if dataset[i][2]==0:
				SUM0x+=dataset[i][0]
				COUNT0x+=1
				SUM0y+=dataset[i][1]
				COUNT0y+=1
			
			else:
				SUM1x+=dataset[i][0]
				COUNT1x+=1
				SUM1y+=dataset[i][1]
				COUNT1y+=1
			

		

		MEAN[0][0]=SUM0x/COUNT0x
		MEAN[0][1]=SUM0y/COUNT0y
		MEAN[1][0]=SUM1x/COUNT1x
		MEAN[1][1]=SUM1y/COUNT1y
			
			'''
			for kth in range(k-1):
				#sprint("i= ",i," j=",j," kth=",kth)
				if dataset[i][cols-1]==kth:
					SUM[j][kth]+=dataset[i][kth]
					COUNT[j][kth]+=1

					MEAN[kth][j]=SUM[j][kth]/COUNT[j][kth]
			
	return MEAN
	
def findDistance(datasetRow,MEANRow,cols):
	#mean and dataset have same number of columns=n
	#	n=MEANRow.shape
	MuneebsSum=0
	global count
	for j in range(cols):
		MuneebsSum+=pow((datasetRow[j]-MEANRow[j]),2)
	distance=math.sqrt(MuneebsSum)
	return distance

def plotNow(MEAN,dataset,initialplot=0):
	k,n=MEAN.shape
	rows,cols=dataset.shape

	#Lets give each mean a different color
	#I dont know how to put numeri colors
	
	colors=["r","b","g","c","m","y"]
	for i in range(k): #i represents i-th MEAN for each cluster
		#and we can plotscatter only 2D points
		plt.scatter(MEAN[i][0], MEAN[i][1], color = colors[i], marker = "o", s = 50)
	#so all means have been scattered on the plot

	x=np.zeros(rows)
	y=np.zeros(rows)

	#this is for the plotting things
	'''for row in dataset:
		x.append(row[0])
		y.append(row[1])

	OLD WAYS BOTH OF THEM
	for i in range(rows):
		x[i]=dataset[i][0]
		y[i]=dataset[i][1]
	'''
	
	#on the basis of class size
	for row in range(rows):
			if initialplot==1:
				plt.scatter(dataset[row,0],dataset[row,1],color = "y", marker = "o", s = 10)
			else:
				plt.scatter(dataset[row,0],dataset[row,1],color = colors[int(dataset[row,2])], marker = "o", s = 10)
	plt.xlabel('x') 
	plt.ylabel('y') 

	plt.show()

def MuneebsKMeansMain():
	##############Muneebs STEP1##########################

	#Define Training Data
	dataset = np.genfromtxt('./kmeans.csv', delimiter=',')
	#print(dataset)
	m,n = dataset.shape #it has m rows and n cols
	n=n-1 #if n<=3; can be easily plotted (x,y,class) class can be used for actual {testing}
	
	##############Muneebs STEP2##########################
	#Get K-Cluster size from user
	k=input("Enter value of K (No of clusters): ")
	k=int(k)
	if k >= m: #error handling on K
		print("Bad idea. No of clusters >> Total tuples in CSV file>>> ")



	##############Muneebs STEP3##########################
	#Inititialize Means, Remembr::: No of Means = no of clusters (k) 
	#I can use intelligent guessing to find the means but leave that part for now
	MEAN=np.zeros(shape=(k,n),dtype='float')
	#There are k no of means;;;;;;;and each means have n variables i,e. mean along x,y in case n=3 (x,y,class)
	MEAN=getInitialMean(MEAN)
	print(MEAN)


	##############Muneebs STEP4##########################
	#Lets plot everything till now
	#if no of variables x,y,z,.... are more than two, how can we plot them on 2D?
	#Ask Sir about this, last time Zeeshan Sir talked about DIM_REDUCTION.
	if n==2:
		#good to go :D
		plotNow(MEAN,dataset,1)


	##############Muneebs STEP5##########################
	#frOM this point, lets do actual calculation
	#REPEAT Step5.1 and Step5.2 until n number of iterations
	#or intelligently store if means dont change
	iterations=5
	for it in range(iterations):
		#>>>>>Step5.1>>>>> 
		'''FOR EACH point in 2D plane, calculate its EUCLEADIAN/CITYBLOCK distance from
			each mean point. Whatever it is near to, update its color to that mean's color
			Also update, its class (i.e. 2) in dataset(0,1,2) to be equal to that means number
			say if it is ith row, and near to mean[1], then update dataset[i][2] = 1 
		'''
		distancevec=np.zeros(shape=(m,k),dtype='float32')
		#distancevec= np.zeros((k*m,2), dtype=np.float32)
		for i in range(m):
			for kth in range (k):
				distancevec[i][kth]=dist=findDistance(dataset[i],MEAN[kth],n)
				print(dist)
				
		print(distancevec)

		for i in range(m):
			minimumdistance=distancevec[i][0]
			for kth in range (k):
				if distancevec[i][kth]<=minimumdistance:
					minimumdistance=distancevec[i][kth]
					dataset[i][2]=kth

		print(dataset)
		plotNow(MEAN,dataset)
					
		#print(distancevec.dtype)
		#distancevec=np.sort(distancevec,axis=0)
		#dataset[i][2]=distancevec[i][1]  #classno starts from 0

		#>>>>>Step5.2>>>>>
		'''FIND thw new mean using datasets[i][2] column, 
		which was udated in the previous step 5.1
		'''
		updateMean(dataset,MEAN)


	return



if __name__=="__main__":
	MuneebsKMeansMain()
