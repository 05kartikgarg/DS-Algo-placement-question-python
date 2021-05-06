# Python program to print print all primes in a range 
# using concept of Segmented Sieve 
from math import floor, sqrt

def simpleSieve(limit, primes): 
	mark = [False]*(limit+1) 
	
	for i in range(2, limit+1): 
		if not mark[i]: 
			primes.append(i) 
			for j in range(i, limit+1, i): 
				mark[j] = True
				
def primesInRange(low, high):
	limit = floor(sqrt(high)) + 1
	primes = list() 
	simpleSieve(limit, primes)
	n = high - low + 1
	mark = [False]*(n+1)
	for i in range(len(primes)): 
		loLim = floor(low/primes[i]) * primes[i] 
		if loLim < low: 
			loLim += primes[i] 
		if loLim == primes[i]: 
			loLim += primes[i]
		for j in range(loLim, high+1, primes[i]): 
			mark[j-low] = True
	for i in range(low, high+1): 
		if not mark[i-low]: 
			print(i, end = " ") 


low,high=map(int,input().split())
primesInRange(low, high) 
