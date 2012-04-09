target = 13195

def determinePrime(x):
	for number in range(2, x):
		if x % number == 0:
			return False
			
	return True

candidates = xrange(2, target+1)
primes = []

for n in candidates:
	if determinePrime(n):
		primes.append(n)
		
primeFactors = []
		
for number in primes:
	if target % number == 0:
		primeFactors.append(number)
		


print primeFactors[len(primeFactors)-1]


		
	