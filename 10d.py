#in this program we implement the sieve of eratosthenes - using set operations - in order to build a list of all primes below 2M, and then we sum them.

candidates = set(range(3, 2000000, 2))
usedPrimes = set([2])


p = min(candidates - usedPrimes)

while p*2 <= 1999999: 
	z = len(candidates)
	candidates = candidates - set(range(2*p, max(candidates)+1, p))
	
	usedPrimes = usedPrimes | set([p])
	p = min(candidates - usedPrimes)
	if z == len(candidates):
		break

#now we sum the primes
sumOfPrimes = 0
for prime in candidates | usedPrimes:
	sumOfPrimes += prime
	
print sumOfPrimes