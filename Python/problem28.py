
total = 1
for i in range(1,501):
	total += (2*i+1)**2
	total += (2*i+1)**2 - 2*i
	total += (2*i+1)**2 - 4*i
	total += (2*i+1)**2 - 6*i
print "Total:",total
