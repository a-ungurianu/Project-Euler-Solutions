
def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

def lcm(a,b):
	return (a*b)/gcd(a,b)


number = lcm(1,2)

for i in range(3,21):
	number = lcm(number,i)

print(number)
