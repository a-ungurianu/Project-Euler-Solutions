from pemath import get_digits

LIMIT = 1000000


def sum5Dig(nr):
	return sum(i**5 for i in get_digits(nr))


total = 0

for i in range(2,LIMIT):
	if i == sum5Dig(i):
		print i
		total += i

print "Total: ", total