# Import time module
import time

def fib(n):
    # initial condition
    if (n < 2):
        return (n)
    else:
        # return the number before and the number before the number before
        return (fib(n - 1 ) + fib(n - 2))

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
