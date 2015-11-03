import itertools
from fractions import *


def e_coeffs():
    yield 2

    for k in itertools.count(1):
        yield 1
        yield 2*k
        yield 1

coeffs_iter = e_coeffs()

def inverse(f):
    return Fraction(f.denominator,f.numerator)

def calc_e(k):
    if k == 0:
        return next(coeffs_iter)

    return Fraction(next(coeffs_iter)) + inverse(calc_e(k-1))

print(sum(list(map(int,list(str(calc_e(99).numerator))))))