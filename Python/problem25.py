
f1,f2 = 1,1

cnt = 2

while len(str(f2)) < 1000:
	f1,f2 = f2,f1+f2
	cnt+=1

print cnt
