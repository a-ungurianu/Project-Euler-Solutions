from itertools import permutations
import operator


def check(sNumber):
    if(int(sNumber[1:4])%2 != 0):
        return False
    if(int(sNumber[2:5])%3 != 0):
        return False
    if(int(sNumber[3:6])%5 != 0):
        return False
    if(int(sNumber[4:7])%7 != 0):
        return False
    if(int(sNumber[5:8])%11 != 0):
        return False
    if(int(sNumber[6:9])%13 != 0):
        return False
    if(int(sNumber[7:10])%17 != 0):
        return False
    return True

pSum = 0;

def tuple_str(tupl):
    return reduce(operator.add,tupl)

for perm in permutations("1234567890"):
    sNumber = tuple_str(perm)
    if sNumber[0] != '0':
        if check(sNumber):
            pSum += int(sNumber)

print pSum