from itertools import count
from pemath import is_prime

bottom_right = lambda x: (2*x+1)**2
bottom_left = lambda x: (2*x+1)**2 - 2*x
top_left = lambda x: (2*x+1)**2 - 4*x
top_right = lambda x: (2*x+1)**2 - 6*x


count_primes = 0
count_total = 1

#primes = PrimeNumbers(int(4e8))

for x in count(1):
    count_total += 4
    if(is_prime(bottom_left(x))):
        count_primes += 1
    if(is_prime(top_left(x))):
        count_primes += 1
    if(is_prime(top_right(x))):
        count_primes += 1

    ratio = float(count_primes)/count_total
    if ratio*100 < 10:
        print(x,ratio)
        break
    if x % 100 == 0:
        print(x,ratio)

