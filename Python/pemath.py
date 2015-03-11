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

class Factorials:
	def __init__(self,up_to=None,n=None):	
		if up_to != None:
			self.factorials = [1]
			x = 1
			while(self.factorials[-1]*x <= up_to):
				self.factorials.append(self.factorials[-1]*x)
				x+=1
		elif n != None:
			self.factorials = [1]
			for x in range(1,n+1):
				self.factorials.append(self.factorials[-1]*x)
		else:
			raise ValueError	

	def get_factorials(self):
		return self.factorials
	def get_nth_factorial(self,n):
		return self.factorials[n]
	def comb(self,n,k):
		return self.factorials[n]/(self.factorials[k]*self.factorials[n-k])

def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

def lcm(a,b):
	return (a*b)/gcd(a,b)

def digit_sum(n):
	return reduce(operator.add,(int(c) for c in str(abs(n))))
