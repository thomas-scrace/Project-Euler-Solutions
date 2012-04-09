import sys

# this program returns prime factors of any number

def iterate(primes, c):
	for d in primes:
		if d > c**0.5:
			return 1
		if c/d == float(c)/float(d):
			return 0
	return 1

def primeGen(n):
	#returns a list of primes less than sqrt(n)
	primes = [2]
	c = 3
	while (c < n**0.5):
		if iterate(primes, c):
			primes.append(c)
			c += 1
		else:
			c +=1
	return primes
		
		
	

def factorise(n):
	primes = primeGen(n)
	factors = []
	for d in primes:
		if (n/d == float(n)/float(d)):
			factors.append(d)
	print factors
			
		
		
factorise(int(sys.argv[1]))
