

with open("input.txt") as f:
	s = 0
	for line in f:
		s+= int(line)
	print str(s)[:10]
