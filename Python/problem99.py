import math

numbers = []

with open("base_exp.txt","r") as f:
    i = 1
    for line in f.readlines():
        b,e = (int(x) for x in line.split(","))
        val = e * math.log(b) 
        numbers.append((val,(b,e),i))
        i += 1

numbers.sort()

print numbers[-1][2]