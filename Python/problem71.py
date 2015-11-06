from fractions import Fraction
import math

maxFr = Fraction(2,5)

for d in range(1,1000001):
    n = int(math.floor(3.0*d/7))
    while 7*n < 3*d:
        cur = Fraction(n,d)
        if cur > maxFr:
            maxFr = cur
        n+=1

print maxFr