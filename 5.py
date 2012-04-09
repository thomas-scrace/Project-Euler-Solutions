#euler 5: this program returns the smallest positive number that is divisible evenly by all the numbers from 1 to 20

def divisible(n):
	if n == 0:
		return 0
	for d in range(2, 21):
		if n/d == float(n)/float(d):
			continue
		else:
			return 0
	return 1
	
c = 0
while not divisible(c):
	c += 20
	
print c