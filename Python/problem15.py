from math import factorial

def combs(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))

N = 20
M = 20

print combs(N+M,N)
