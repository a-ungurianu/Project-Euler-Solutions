import pemath

primes = pemath.PrimeNumbers(1000000)

max_x = 0
max_poly = ()

def get_val(x,a,b):
	return x*x + a*x + b

b_candidates = primes.get_first_primes(1000) + [-x for x in primes.get_first_primes(1000)]

for a in range(-1000,1001):
	for b in b_candidates:
		x = 0
		while(primes.is_prime(get_val(x,a,b))):
			x+=1
		if(max_x < x):
			max_x = x
			max_poly = (1,a,b)
	if(a%100 == 0):
		print a
print max_x
print max_poly