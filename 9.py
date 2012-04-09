squares = []

for number in range(1001):
	squares.append(number**2)
	
sos = []	
for number in range(1001):
	sums = []
	for sq in squares[2:number]:
		for p in squares[sq:number]:
			sums.append(sq+p)
	if number in sums:
		sos.append(number)
	