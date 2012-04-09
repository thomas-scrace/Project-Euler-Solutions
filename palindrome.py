#Euler problem 4: this program finds the highest palindromic product of two three-digit numbers

def isPalindrome(n):
	c = str(n)
	f = 0
	l = len(c)-1
	while l > f:
		if c[f] == c[l]:
			f += 1
			l -= 1
			continue
		else:
			return 0
	return 1

palindromes = [101]
	
for d in range(100, 1000):
	for e in range (100, 1000):
		if isPalindrome(d*e) and d*e > palindromes[0]:
			palindromes[0] = d*e
			
print palindromes[0]
	