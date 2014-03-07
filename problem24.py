from itertools import permutations

cnt = 1

for i in permutations(range(10)):
	if cnt == 1000000:
		print i
		break
	cnt+=1
