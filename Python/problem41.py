from itertools import permutations
from pemath import is_prime

def get_pandigitals():
	for sz in range(2,8):
		for perm in permutations(range(1,sz+1),sz):
			if perm[-1] % 2 != 0:
				yield reduce(lambda x,y: x*10+y,perm,0)



for x in [x for x in get_pandigitals()][::-1]:
	if is_prime(x):
		print x
		break