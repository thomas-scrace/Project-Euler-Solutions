#in this program we implement the sieve of eratosthenes in order to build and list of all primes below 10M, and then we sum them.

candidates = range(2, 2000000)
q = 0
while q <= (len(candidates)-1):
	p = candidates[q]
	i = 2*p

	while (i <= candidates[len(candidates)-1]):
		if i in candidates:
			candidates.remove(i)
		i += p
	
	q += 1
	print len(candidates)
	
print candidates
