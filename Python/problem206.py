import re

def matches(number):
    strNr = str(number)
    if len(strNr) != 19:
        return False

    if strNr[::2] == "1234567890":
        return True

    return False


for i in range(10**6,10**7+1):
    if(i%10**5 == 0):
        print(i/10**5)
    res = int("1"+str(i)+"30")**2

    if(matches(res)):
        print("1"+str(i)+"30",res)
        break
        
    res = int("1"+str(i)+"70")**2

    if(matches(res)):
        print("1"+str(i)+"70",res)
        break