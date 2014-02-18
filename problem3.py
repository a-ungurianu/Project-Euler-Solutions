
def GetPrimeFactors(n):
	d = 2
	factors = []
	while n != 1:
		if n%d == 0:
			factors.append(d)
		while n%d == 0:
			n /= d;
		d += 1
	return factors

print GetPrimeFactors(600851475143)[-1]
