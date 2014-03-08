



def isCircularPrime(n):
	def isPrime(n):
	    '''check if integer n is a prime'''
	    # make sure n is a positive integer
	    n = abs(int(n))
	    # 0 and 1 are not primes
	    if n < 2:
	        return False
	    # 2 is the only even prime number
	    if n == 2: 
	        return True    
	    # all other even numbers are not primes
	    if not n & 1: 
	        return False
	    # range starts with 3 and only needs to go up the squareroot of n
	    # for all odd numbers
	    for x in range(3, int(n**0.5)+1, 2):
	        if n % x == 0:
	            return False
	    return True

	def next(n):
		s = str(n)
		return int(s[1:]+s[0])

	if str(n).find('0') != -1:
		return False

	for i in range(len(str(n))):
		if not isPrime(n):
			return False
		n = next(n)

	return True

cnt = 0

for i in range(1,10**6):
	if isCircularPrime(i):
		print i
		cnt+=1

print cnt
