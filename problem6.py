
def squareOfSum(n):
	return sum([x for x in range(1,n+1)])**2
def sumOfSquare(n):
	return sum([x**2 for x in range(1,n+1)])

print(squareOfSum(100)-sumOfSquare(100))
