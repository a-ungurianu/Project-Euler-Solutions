
def X(n1,n2,n3):
    return n1^n2^n3

count = 0

for i in xrange(1,(1<<30)+1):
    if X(i,2*i,3*i) == 0:
        count+=1

print count