import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

#Decison tree i,pleeted by MUNEEB AHMED MTECH 1ST YR JMI

def calculateCondProb(attrib,target,val1,val2,no_rows):


	count1=0
	count2=0

	for i in range(no_rows):
		if target[i]==val2:
			if attrib[i]==val1:
				count1=count1+1

	for i in range(no_rows):
		if attrib[i]==val1:
			count2=count2+1	
	P=round((count1/count2),3)
	return P


def calculateProb(A,B):
	#print(A)
	factor=A/B
	return factor

def calculateInfoDatabase(D,no_rows):
	#print(D)
	total=0
	values=list(set(D))
	count=dict()

	for value in values:
		count[value]=0
		for row in range(no_rows):
			#print(D[row])
			#print(option)
			if D[row]==value:
				count[value]=count[value]+1
				total=total+1
			

	print('Information of System', count, ' Total=',total)

	I=0
	for value in values:
			P=calculateProb(count[value],total)
			#print(P)
			I+=(-1)*P*(math.log2(P))
			#print(I)
	
	print(round(I,3))
	return(round(I,3))

def calculateEntropyOnEachAttrib(target, attrib, colname,no_rows):
	#print(target)
	#print(attrib)
	totalA=0
	totalT=0
	valuesA=list(set(attrib))
	valuesT=list(set(target))
		
		
	countA=dict()
	countT=dict()

	for valueA in valuesA:
			countA[valueA]=0
			for row in range(no_rows):
				#print(D[row])
				#print(option)
				if attrib[row]==valueA:
					countA[valueA]=countA[valueA]+1
					totalA=totalA+1

	
	for valueT in valuesT:
			countT[valueT]=0
			for row in range(no_rows):
				#print(D[row])
				#print(option)
				if target[row]==valueT:
					countT[valueT]=countT[valueT]+1
					totalT=totalT+1	
	#print('iof ', colname, 'is ', countT, ' Total=',totalT)
	E=0
	split=0
	for i in valuesA:
		for j in valuesT:

			P=calculateCondProb(attrib,target,i,j, no_rows)
			#print (P)
			#print( countA[i])

			#print('\n')

			Factor=countA[i]/totalA
			split+=Factor
			if P!=0:
				E+=(-1)*Factor*P*(math.log2(P))
			#print('P= ',P, ' Factor=',Factor,' E=',E)

	#print('Entropy of ', colname , ' =',E)
	return round((E/split),3)			


def calculateInformation(dataset,cols):
	no_rows,no_cols=dataset.shape
	
	#target column br the last column	
	targetcol=no_cols-1


	formattedcols=cols.copy()
	formattedcols.pop(targetcol)


	for epoch in range(no_cols-1):

		print("\n*****************************************************\n                          Epoch", epoch,"\n******************************************************\n")
		#1. INFORMATION OF THE DATABASE
		I=calculateInfoDatabase(dataset[cols[targetcol]], no_rows)
		maxgain=0
		node='A'
		#2. calculate entropy of each attrib
		for col in formattedcols:
			E=calculateEntropyOnEachAttrib(dataset[cols[targetcol]], dataset[col],col, no_rows)
			Gain= I-E
			print('Split Ratio of ', col , ' =',E, ' GAIN Ratio= ',Gain)
			if maxgain<=Gain:
				node=col
				maxgain=Gain

		print(epoch,'SelectedNode: ',node)
		index_node=formattedcols.index(node)
		formattedcols.pop(index_node)

			#print(cols)
	 
			#print(dataset[col]) 
				
			#print(dataset[cols[targetcol]]) 
				
			#do for each column, calculate INFORMATION Info of db based in attributes
			#exept last column *taken car of in the for loop)
			#P=calculateProb(dataset[col],dataset[cols[targetcol]])
			#I+=(-1)*(P)*math.log2(P) 





def MuneebsDTMain():
	print("ORIGINAL DATA:")


	dataset= pd.read_csv('./DTextradata.csv')
	print(dataset)

	#LIST ALL COLUMNS
	cols=list(dataset.columns.values)
	#print(cols)
	

	calculateInformation(dataset,cols)


	#calculateEntropyOnEachAttrib(dataset)

	#row,col=dataset.shape
	#for epoch in range (1):
		#stopiing critea for DT
		#clacultate I(D)
	



if __name__=="__main__":
	MuneebsDTMain()
