"""this program finds the only pythagorean triplet whose three elements sum to
1000, and then prints the product of its three elements just for fun I rewrote
it as a list comprehension.""" 

"""however, because we cannot break out of the comprehension as soon as the
answer is found, this version runs about twice as long as the previous version.
Not quite so neat."""

print [(x, y, z) for x in range(1001) for y in range(x+1, 1001) for z in
			range(y+1, 1001) if x**2+y**2==z**2 if x+y+z==1000]

