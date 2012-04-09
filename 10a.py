#in this program we implement the sieve of eratosthenes in order to build and list of all primes below 10M, and then we sum them.

candidates = range(3, 100000, 2)

q = 0
while candidates[q]*2 <= 99999:
	y = len(candidates)
	p = candidates[q]
	i = 2*p

	while (i <= max(candidates)):
		if i in candidates:
			candidates.remove(i)
		i += p
	
	q += 1
	z = len(candidates)
	print z
	if z == y:
		break

candidates.insert(0, 2)	
print candidates