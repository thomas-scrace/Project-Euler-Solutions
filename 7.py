#euler 7: this program returns the 10001st prime

def iterate(primes, c):
	for d in primes:
		if d > c**0.5:
			return 1
		if c/d == float(c)/float(d):
			return 0
	return 1

def primeGen():
	primes = [2]
	c = 3
	while (len(primes)<10002):
		if iterate(primes, c):
			primes.append(c)
			c += 1
		else:
			c +=1
	print primes[10000]
	
primeGen()
	
