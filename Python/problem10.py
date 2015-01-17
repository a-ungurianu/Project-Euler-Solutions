

N = 2*10**6

isPrime = [True]*N

primes = []

for d in range(2,N):
	if isPrime[d]:
		primes.append(d)
		i = d*d
		while i < N:
			isPrime[i]=False
			i+=d

print(sum(primes))
