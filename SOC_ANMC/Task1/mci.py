import numpy as np
# Program to multiply two matrices (vectorized implementation)
print("Enter Time and starting point")
time = input()
start= input()

# Program to multiply two matrices (vectorized implementation)

# take a 3x3 matrix
A = np.array([[0.2,0.7,0.1],
	[0.4, 0, 0.6],
	[0.1,0.8,0.1]])
result= np.array([[0.2,0.7,0.1],
	[0.4, 0, 0.6],
	[0.1,0.8,0.1]])
for x in range(int(time)):
	result = np.dot(A,A)
print(result[int(start),:])
