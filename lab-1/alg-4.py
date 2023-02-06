# Import time module
import time

# Fibonacci Series using Dynamic Programming
def fib(n):
     
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
     
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

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
