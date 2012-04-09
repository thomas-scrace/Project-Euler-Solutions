target = 13195

def determinePrime(x):
	for number in range(2, x):
		if x % number == 0:
			return False
			
	return True
	
factors = []

for number in xrange(2, target):
	if target % number ==0:
		factors.append(number)
		
		
primeFactors = []

for number in factors:
	if determinePrime(number):
		primeFactors.append(number)
		
print primeFactors[len(primeFactors)-1]


	