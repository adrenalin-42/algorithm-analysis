# Import time module
import time

def fib(n):
    i = 1 # first term
    j = 0 # second term
    k = 1
    while (k <= n): # repeat the loop `n` times
        j = i + j # second term = first term + second term
        i = j - i # first term = second term - first term
        k += 1

    return (j)

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
