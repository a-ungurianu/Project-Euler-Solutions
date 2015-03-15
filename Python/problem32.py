
def is_pandigital_product(a,b):
	digits = [False]*10

	for c in str(a):
		if digits[int(c)]:
			return False
		digits[int(c)] = True

	for c in str(b):
		if digits[int(c)]:
			return False
		digits[int(c)] = True

	for c in str(a*b):
		if digits[int(c)]:
			return False
		digits[int(c)] = True

	for i in range(1,10):
		if digits[i] == False:
			return False
	return True


sums = set() 

for a in range(2,100):
	for b in range(123,10001/a +1):
		if(is_pandigital_product(a,b)):
			sums.add(a*b)

total = 0
for i in sums:
	total += i
print total