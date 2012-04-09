#this program finds the only pythagorean triplet whose three elements sum to 1000, and then prints the product of its three elements

#I refactored this as a function in order to be able to use 'return' to break out of the nested loops as soon as the answer is found. Bizarrely, however, wrapping
# the code up in a function shaved about 5 seconds (beyond that saved by breaking out of the loop as soon as possible) off the time of the non-functioned code. I can
# only surmise that python is pre-interpreting the code down to bytecode before running the function, instead of dynamically interpreting it line by line.

def findTrip():
	for x in range(1001):
		for y in range(x+1, 1001):
			for z in range (y+1, 1001):
				if x**2 + y**2 == z**2:
					if x + y + z == 1000:
						print x, y, z
						return
						#print x*y*z
						
findTrip()

					

					