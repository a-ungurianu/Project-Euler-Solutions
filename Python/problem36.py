from pemath import is_palindrome, is_binary_palindrome

palSum = 0

for i in range(1,1000001) :
	if i%2 and is_palindrome(i) and is_binary_palindrome(i) :
		palSum += i	


print palSum
