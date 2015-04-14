from pemath import PrimeNumbers, get_digits
import itertools

primes = PrimeNumbers(10000)

for nr in (p for p in primes.get_primes() if p >= 1000):
	if 0 in get_digits(nr):
		continue
	
	numbers = [ reduce(lambda a,x:a*10 + x,digits[::-1],0) for digits in itertools.permutations(get_digits(nr))]
	numbers = list(set(numbers))
	numbers = [number for number in numbers if primes.is_prime(number)]
	numbers.sort()

	for i in range(len(numbers)):
		for j in range(i+1,len(numbers)):
			ratio = numbers[j] - numbers[i]
			for k in range(j+1,len(numbers)):
				if numbers[k] - numbers[j] == ratio and numbers[i] != 1487:
					print numbers[i],numbers[j],numbers[k]
					