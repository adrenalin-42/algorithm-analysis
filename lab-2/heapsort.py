# Driver code
import random

# Import time module
import time

# Import matplotlib
import matplotlib.pyplot as plt


# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap


def heapify(arr, N, i):
	largest = i # Initialize largest as root
	l = 2 * i + 1	 # left = 2*i + 1
	r = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < N and arr[largest] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < N and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapify the root.
		heapify(arr, N, largest)

# The main function to sort an array of given size


def heapSort(arr):
	N = len(arr)

	# Build a maxheap.
	for i in range(N//2 - 1, -1, -1):
		heapify(arr, N, i)

	# One by one extract elements
	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)


def getTime(min, max, numRange):

	# Generate a random array of 10 integers between 1 and 100
	array = [random.randint(min, max) for _ in range(numRange)]

	# record start time
	start = time.time()

	heapSort(array)

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
plt.title('Heap Sort Graph')

# Display plot
plt.show()