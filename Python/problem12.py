from math import sqrt
import operator

def genTriangular():
	n = 1
	i = 2
	yield n
	while True:
		n += i
		i +=1
		yield n


def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
    
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d

def divCount(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  return reduce(operator.mul, powers_plus, 1)

for i in genTriangular():
	if divCount(i) >= 500:
		print i
		break
