'''
Euler problem 12.
Thomas Scrace
March 2012
'''

'''
What is the first triangle number to have over 500 divisors?
'''

def num_divisors(n):
	m = 2
	d = 2
	while m <= n / 2:
		if n % m == 0:
			d += 1
		m += 1
	return d

def get_triangle(n):
	t = 0
	for i in range(1, n + 1):
		t += i
	print "\t triangle is %d" % t
	return t

def get_tri(n):
	low = 2
	high = 2
	while True:
		print "Trying %d" % high
		high_div = num_divisors(get_triangle(high))
		print "\t\t %d divisors" % high_div
		if high_div >= n:
			if high_div == n:
				candidate = n
				while num_divisors(get_triangle(candidate)) == n:
					candidate -= 1
				return candidate + 1
			high = low + ((high - low) / 2)
		else:
			low = high
			high *= 2


print get_tri(501)
