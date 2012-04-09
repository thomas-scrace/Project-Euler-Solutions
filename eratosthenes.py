target = 3572

p = 2
q=1

candidates = range(2, target)

while p**2 <= target:
	for number in candidates:
		if number % p == 0 and number !=p:
			candidates.remove(number)
	p = candidates[q]
	q += 1
	
print candidates
		
	