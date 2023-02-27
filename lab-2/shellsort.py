# Python3 program for implementation of Shell Sort
# Driver code
import random

# Import time module
import time

# Import matplotlib
import matplotlib.pyplot as plt

def shellSort(arr, n):
	# code here
	gap = n // 2
	
	
	while gap > 0:
		j = gap
		# Check the array in from left to right
		# Till the last possible index of j
		while j < n:
			i = j - gap # This will keep help in maintain gap value
			
			while i >= 0:
				# If value on right side is already greater than left side value
				# We don't do swap else we swap
				if arr[i + gap] > arr[i]:

					break
				else:
					arr[i + gap], arr[i] = arr[i], arr[i + gap]

				i = i - gap # To check left side also
							# If the element present is greater than current element
			j += 1
		gap = gap // 2


def getTime(min, max, numRange):

	# Generate a random array of 10 integers between 1 and 100
	array = [random.randint(min, max) for _ in range(numRange)]

	# record start time
	start = time.time()

	shellSort(array, len(array))

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
plt.title('Shell Sort Graph')

# Display plot
plt.show()