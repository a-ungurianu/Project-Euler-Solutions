from math import ceil
from itertools import count

p = lambda x:2*x + ceil(float(x)/2)
t = lambda x:4*x + 1


for x in count(1):
    if p(x)/t(x) <= 1/10:
        print(x)
        break

    if x % 100 == 0:
        print(str(x) + " " + str(p(x)/t(x)))