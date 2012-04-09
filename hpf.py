import sys

# this program returns the highest prime factor of any number



def isprime(x):
	if x < 2:
		return 0
	n = 2
	while (n < x):
		if x/n == float(x)/float(n):
			return 0
		else:
			n += 1
	
	return 1

def factorise(n, d):
	if isprime(n):
		print "hpf=%d" % n
		return
	if isprime(d):
		if n/d == float(n)/float(d):
			factorise(n/d, 2)
		else:
			factorise(n, d+1)
	else:
		factorise(n, d+1)
		
		
factorise(int(sys.argv[1]), 2)
	