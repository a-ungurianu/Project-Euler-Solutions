import itertools
from fractions import *


def sqrt2_coeffs():

    yield 1
    for k in itertools.count(1):
        yield 2


def inverse(f):
    return Fraction(f.denominator,f.numerator)


part_frac =[]


import sys
sys.setrecursionlimit(1200)
def generate_2s(k):
    if k == 0:
        return 2

    part_frac.append(Fraction(2) + inverse(generate_2s(k-1)))
    return part_frac[-1]

def sqrt2(k):
    return Fraction(1) + inverse(part_frac[k])

generate_2s(1000)


def check(fr):
    if len(str(fr.numerator)) > len(str(fr.denominator)):
        return True
    return False


count = 0
for i in xrange(1000):
    if check(sqrt2(i)):
        count += 1

print count

