# Import time module
import time

# Helper function that multiplies
# 2 matrices F and M of size 2*2,
# and puts the multiplication
# result back to F[][]

# Helper function that calculates
# F[][] raise to the power n and
# puts the result in F[][]
# Note that this function is
# designed only for fib() and
# won't work as general
# power function
def fib(n):
	F = [[1, 1],
		[1, 0]]
	if (n == 0):
		return 0
	power(F, n - 1)
	
	return F[0][0]

def multiply(F, M):

	x = (F[0][0] * M[0][0] +
		F[0][1] * M[1][0])
	y = (F[0][0] * M[0][1] +
		F[0][1] * M[1][1])
	z = (F[1][0] * M[0][0] +
		F[1][1] * M[1][0])
	w = (F[1][0] * M[0][1] +
		F[1][1] * M[1][1])
	
	F[0][0] = x
	F[0][1] = y
	F[1][0] = z
	F[1][1] = w

def power(F, n):

	M = [[1, 1],
		[1, 0]]

	# n - 1 times multiply the
	# matrix to {{1,0},{0,1}}
	for i in range(2, n + 1):
		multiply(F, M)

def getTime(n: int):
	# record start time
	start = time.time()

	fib(n)

	# record end time
	end = time.time()
	
	# print the difference between start
	# and end time in milli. secs
	print("The time of execution for fib(", n, ") is:",
		(end-start), "s")

getTime(5)
getTime(10)
getTime(15)
getTime(20)
getTime(25)
getTime(30)
getTime(35)
getTime(40)
getTime(50)
getTime(100)
getTime(1000)
getTime(10000)
getTime(100000)
getTime(1000000)