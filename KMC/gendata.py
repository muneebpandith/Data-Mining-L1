import numpy as np
import matplotlib.pyplot as plt
import csv

# Create data
N = 250


#array of 250 elements


dataset=np.zeros(shape=(500,3))

x1 = np.random.rand(N)
y1 = np.random.rand(N)
colors1=(0,0,1)
x2 = np.random.rand(N)
y2 = np.random.rand(N)
colors2=(0,1,0)

for i in range (250):
	x1[i] = i
	y1[i]*=100
	dataset[i][0]=x1[i]
	dataset[i][1]=y1[i]
	dataset[i][2]=1
	#CLASS1

for i in  range (250):
	#CLASS2
	x2[i]=i+280

	y2[i]*=100
	dataset[i+250][0]=x2[i]
	dataset[i+250][1]=y2[i]
	dataset[i+250][2]=2

print(dataset)
# Plot
i=0

#writeFile.close()

np.savetxt("foo.csv", dataset, delimiter=",")

plt.scatter(x1, y1, s=10, c=colors1, alpha=0.5)
plt.scatter(x2, y2, s=10, c=colors2, alpha=0.5)

plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()