from pemath import is_palindrome

pals = []

for i in range(100,1000):
	for j in range(100,i+1):
		if is_palindrome(i*j):
			pals.append(i*j)

print(max(pals))
