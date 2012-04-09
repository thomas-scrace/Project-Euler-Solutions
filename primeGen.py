def iterate(primes, c):
	for d in primes:
		if d > c**0.5:
			return 1
		if c/d == float(c)/float(d):
			return 0
	return 1

def primeGen(n):
	primes = [2]
	c = 3
	while (c < n):
		if iterate(primes, c):
			print (float(c)/float(n))*100
			primes.append(c)
			c += 1
		else:
			c +=1
	return primes