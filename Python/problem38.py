from pemath import is_pandigital

lastPan = 0
for i in range(10**2,10**4):
	nr = int("9"+str(i))
	if is_pandigital(int(str(nr)+str(nr*2))):
		lastPan = str(nr)+str(nr*2)
print lastPan