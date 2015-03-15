from pemath import pentagonal_numbers, is_pentagonal
import itertools

def take(n,iterable):
	return list(itertools.islice(iterable,n));

pentagonals = take(3000,pentagonal_numbers())

min_diff = 123123123213

for i in range(len(pentagonals)):
	for j in range(i+1, len(pentagonals)):
		if(is_pentagonal(pentagonals[j]-pentagonals[i]) and
		   is_pentagonal(pentagonals[j]+pentagonals[i])):
			min_diff = min(min_diff,pentagonals[j]-pentagonals[i])
print min_diff


