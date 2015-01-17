from itertools import count


s = ""

for i in count(1):
	s+=str(i)
	if len(s) > 10**6:
		break

p = 1

prod = 1

print s[999999]

for i in range(6):
	prod*=int(s[p-1])
	p*=10

print prod
