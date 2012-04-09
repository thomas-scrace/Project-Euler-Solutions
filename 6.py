#euler 6: this program gives the difference between the sum of the squares and the square of the sum of the first one hundred natural numbers

def sqOfSum():
	s = 0
	for d in range(1, 101):
		s += d
	return s**2
	
def sumOfSq():
	s = 0
	for d in range(1, 101):
		s += d**2
	return s

print abs(sumOfSq() - sqOfSum())