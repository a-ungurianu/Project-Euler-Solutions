
cache = {}

def collatzLength(n):
	def nextCollatz(n):
		if n%2 == 0:
			return n/2
		return 3*n + 1
	cnt = 1
	initN = n
	while n!=1:
		cnt+=1
		n = nextCollatz(n)
		if n in cache:
			cache[initN] = cache[n]+cnt-1;
			return cache[initN];
	return cnt

maxLen = 0
maxLenI = 0

for i in range(1,1000001):
	cache[i] = collatzLength(i)
	if maxLen < cache[i]:
		maxLen = cache[i]
		maxLenI = i


print maxLenI
