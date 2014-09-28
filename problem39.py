
# generate a list for every integer perimeter value
solutions = [[] for _ in range(1001)]

# get the hypotenuse of the right triangle
def getHyp(a,b):
	from math import sqrt
	return sqrt(a**2+b**2)


# generate distinct pairs of numbers
for a in range(1,1001):
	for b in range(a,1001):
		c = getHyp(a, b)
		#check to see if we got over the perimeter limit
		if a+b+c > 1000:
			break
		if c == int(c):
			solutions[int(a+b+c)].append((a,b,int(c)))

maxSol = (0,0)

for i,s in enumerate(solutions):
	if len(s) >= maxSol[1]:
		maxSol = (i,len(s))

print maxSol
