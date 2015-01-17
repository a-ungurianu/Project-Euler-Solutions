
evenFibSum = 0

f1,f2 = 1,2

while f2 < 4*10**6:
	if f2%2 == 0:
		evenFibSum+=f2
	f1,f2 = f2,f1+f2

print evenFibSum
