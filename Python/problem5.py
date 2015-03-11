from pemath import lcm

number = lcm(1,2)

for i in range(3,21):
	number = lcm(number,i)

print(number)
