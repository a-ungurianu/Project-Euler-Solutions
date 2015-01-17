

def isPalindrome(n):
	s = str(n)
	if len(s) % 2 != 0:
		return False
	else:
		return s[:len(s)/2] == s[:len(s)/2-1:-1]


pals = []

for i in range(100,1000):
	for j in range(100,i+1):
		if isPalindrome(i*j):
			pals.append(i*j)

print(max(pals))
