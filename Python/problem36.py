

def isPalinInB2(x) :
	s = bin(x)[2:]
	if len(s) % 2:
		return s[:len(s)/2][::-1] == s[len(s)/2+1:]
	else:
		return s[:len(s)/2][::-1] == s[len(s)/2:]

def isPalinInB10(x) :
	s = str(x)
	if len(s) % 2:
		return s[:len(s)/2][::-1] == s[len(s)/2+1:]
	else:
		return s[:len(s)/2][::-1] == s[len(s)/2:]

palSum = 0

for i in range(1,1000001) :
	if i%2 and isPalinInB10(i) and isPalinInB2(i) :
		palSum += i	


print palSum
