from pemath import PrimeNumbers

primes = PrimeNumbers(1000000)

max_count = 0
max_prime = 0

for i in range(100):
   
    running_sum = 0
    count = 0
    prime_iter = primes.get_primes()
    for _ in range(i):
        next(prime_iter)

    for prime in prime_iter:
        count += 1
        running_sum += prime
        if running_sum < primes.limit and count > max_count and primes.is_prime(running_sum):
            max_count = count
            max_prime = running_sum

print(max_prime,max_count)

