

def getDigits(nr) :
	while nr != 0:
		yield nr%10
		nr/=10

LIMIT = 1000000


def sum5Dig(nr):
	return sum(i**5 for i in getDigits(nr))


total = 0

for i in range(2,LIMIT):
	if i == sum5Dig(i):
		print i
		total += i

print "Total: ", total