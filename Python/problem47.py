import itertools
from pemath import PrimeNumbers
count = 0

primes = PrimeNumbers(100000)

def get_prime_factor_count(n):
	count = 0
	for d in primes.get_primes():
		if n == 1: break
		if n%d == 0:
			while n%d == 0:
				n /= d
			count += 1
	return count

for i in itertools.count(644):
	if get_prime_factor_count(i) == 4:
		count+= 1
	else:
		count = 0
	if count == 4:
		print i - 3
		break