

d = [1]*10001

for i in range(2,5001):
	for j in range(2*i,10001,i):
		d[j]+=i



amNr = set()

res = 0

for i in range(1,10000):
	x = d[i]
	if x != i and x < 10000 and d[x] == i :
			amNr = amNr | set([i])

print sum(amNr)
