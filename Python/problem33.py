from fractions import Fraction
from itertools import permutations
import operator

resList = []

for c in range(1,10):
    for a in range(1,10):
        for b in range(a+1,10):
            reduced = Fraction(a,b)
            for top in permutations(str(c)+str(a)):
                for bottom in permutations(str(c) + str(b)):
                    if reduced == Fraction(int(top[0]+top[1]),int(bottom[0]+bottom[1])):
                        resList.append(Fraction(int(top[0]+top[1]),int(bottom[0]+bottom[1])))

print reduce(operator.mul,resList)
