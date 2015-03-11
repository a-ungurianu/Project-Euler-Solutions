import math
import operator

class PrimeNumbers:
	def __init__(self,N):
		self.limit = N
		self.precalc_primes(N)

	def precalc_primes(self,N):
		self.sieve = [True]*(N+1)
		for d in range(2,int(N**0.5+1)):
			if self.sieve[d]:
				for i in range(2*d,N+1,d):
					self.sieve[i] = False
		self.primes = [i for i in range(2,N+1) if self.sieve[i]]

	def is_prime(self,n):
		if n > self.limit:
			raise IndexError
		return self.sieve[n]

	def get_first_primes(self,n):
		return self.primes[:n]

	def get_nth_prime(self,n):
		return self.primes[n]

def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

def lcm(a,b):
	return (a*b)/gcd(a,b)

def digit_sum(n):
	return reduce(operator.add,(int(c) for c in str(abs(n))))
