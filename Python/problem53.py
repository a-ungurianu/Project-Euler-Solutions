fact = []
f = 1
for i in range(1,101):
    fact.append(f)
    f *= i
fact.append(f)

def comb(n,k):
    return fact[n]/(fact[k]*fact[n-k])

LIMIT = 100

count = 0
for n in range(1,LIMIT+1):
    for r in range(1,n+1):
        if comb(n,r) > 1000000:
            count+=1

print(count)