from pemath import is_palindrome,reverse_number

def is_lychrel(n):
	for _ in range(50):
		n = n + reverse_number(n)
		if(is_palindrome(n)):
			return False
	return True

count = 0

for n in range(1,10000):
	if is_lychrel(n):
		count += 1

print count
