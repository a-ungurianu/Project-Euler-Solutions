from pemath import is_prime

def isCircularPrime(n):

	def next(n):
		s = str(n)
		return int(s[1:]+s[0])

	if str(n).find('0') != -1:
		return False

	for i in range(len(str(n))):
		if not is_prime(n):
			return False
		n = next(n)

	return True

cnt = 0

for i in range(1,10**6):
	if isCircularPrime(i):
		print i
		cnt+=1

print cnt
