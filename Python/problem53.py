import pemath

factorials = pemath.Factorials(n=102)

LIMIT = 100

count = 0
for n in range(1,LIMIT+1):
    for r in range(1,n+1):
        if factorials.comb(n,r) > 1000000:
            count+=1
            
print(count)