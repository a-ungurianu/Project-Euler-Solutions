from itertools import count

def digSorted(n):
    return sorted(c for c in str(n))

def check(n):
    listRepr = digSorted(n)
    for i in range(2,7):
        if listRepr != digSorted(i*n):
            return False
    return True

for i in count(123456):
    if check(i):
        print i
        break