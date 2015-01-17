from itertools import permutations

def get_pandigitals():
	for sz in range(2,8):
		for perm in permutations(range(1,sz+1),sz):
			if perm[-1] % 2 != 0:
				yield reduce(lambda x,y: x*10+y,perm,0)

def is_prime(x):
	if x < 2: return False
	if x == 2: return True
	for d in range(3,int(x**.5)+1,2):
		if x % d == 0: return False
	return True

for x in [x for x in get_pandigitals()][::-1]:
	if is_prime(x):
		print x
		break