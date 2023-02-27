# Driver code
import random

# Import time module
import time

# Import matplotlib
import matplotlib.pyplot as plt

# Function to find the partition position
def partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# e greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# Function to perform quicksort


def quick_sort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quick_sort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quick_sort(array, pi + 1, high)


def getTime(min, max, numRange):

	# Generate a random array of 10 integers between 1 and 100
	array = [random.randint(min, max) for _ in range(numRange)]

	# record start time
	start = time.time()

	quick_sort(array, 0, len(array) - 1)

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
plt.title('Quick Sort Graph')

# Display plot
plt.show()