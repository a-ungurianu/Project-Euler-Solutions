
def isPan(nr):
	found = set()
	for n in nr:
		if n == '0':
			return False
		if int(n) in found:
			return False
		else:
			found.add(int(n))
	return True

def main():
	lastPan = 0
	for i in range(pow(10,3),pow(10,4)):
		nr = int("9"+str(i))
		if isPan(str(nr)+str(nr*2)):
			lastPan = str(nr)+str(nr*2)
	print lastPan

if __name__ == '__main__':
	main()