# Import time module
import time

def fib(n):
    i = 1
    j = 0
    k = 0
    h = 1
    while (n > 0):
        if (n % 2 != 0): # check for parity
            t = j * h
            j = i * h + j * k + t
            i = i * k + t
        t = h * h
        h = 2 * k * h + t
        k = k * k + t
        n = n // 2
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
