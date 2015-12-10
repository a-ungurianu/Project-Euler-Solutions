# given that the smallest value for n/phi(n) is given when n is prime
# I assumed that the largest value will be given when n is composed of different
# prime factors (e.g. 2*3*5*7...)
# So I just found the largest number smaller than 100000 that is of this form

from pemath import PrimeNumbers

primes = PrimeNumbers(100000)


cur_number = 1

for i in primes.get_primes():
    if cur_number * i <= 1000000:
        cur_number *= i
    else:
        break

print(cur_number)

