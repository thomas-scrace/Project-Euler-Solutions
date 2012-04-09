fibonacci = [1, 2]
result = 0

while fibonacci[len(fibonacci)-1]<= 4000000:
	first = fibonacci[len(fibonacci)-1]
	second = fibonacci[len(fibonacci)-2]
	new = first + second
	fibonacci.append(new)
	
for item in fibonacci:
	if (item % 2) == 0:
		result += item
		
print result
		
	