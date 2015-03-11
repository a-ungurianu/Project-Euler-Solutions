from math import sqrt

def isAbundant(nr):
    initNr = nr
    prod = 1
    for k in range(2,int(sqrt(nr)+1)):
        p = 1
        while nr % k == 0:
            p = p*k + 1
            nr /= k
        prod *= p
    if nr > 1:
        prod *= 1+nr
    return prod > 2*initNr

uppLimit = 28123

abundantNumbers = set()

for i in range(12,uppLimit):
    if i not in abundantNumbers and isAbundant(i):
        for j in range(i,uppLimit,i):
            abundantNumbers.add(j)

abundantNumbers = list(abundantNumbers)

print "Made the numbers",len(abundantNumbers)

formedNumbers = [False]*(uppLimit*2+1)

for i in range(len(abundantNumbers)):
    for j in range(i,len(abundantNumbers)):
        formedNumbers[abundantNumbers[i]+abundantNumbers[j]] = True
        # formedNumbers.add(abundantNumbers[i]+abundantNumbers[j])

print "Made the sums"

finalSum = 0

for i in range(uppLimit):
    if not formedNumbers[i]:
        finalSum += i

print finalSum