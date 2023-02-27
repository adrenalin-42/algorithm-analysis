# Driver code
import random

# Import time module
import time

# Import matplotlib
import matplotlib.pyplot as plt

def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


def getTime(min, max, numRange):

	# Generate a random array of 10 integers between 1 and 100
	array = [random.randint(min, max) for _ in range(numRange)]

	# record start time
	start = time.time()

	mergeSort(array)

	# record end time
	end = time.time()
	
	# print the difference between start
	# and end time in milli. secs
	return (end-start)

x = []
y = []

min = -50000
max = 50000

for i in range(1000, 100000, 1000):
	x += [i]
	y += [getTime(min, max, i)] 


# Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# Create plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('Number of elements')
plt.ylabel('Time (s)')
plt.title('Merge Sort Graph')

# Display plot
plt.show()