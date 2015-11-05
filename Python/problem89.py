
values = [("M",1000),("CM",900),("D",500),("CD",400),
          ("C",100),("XC",90),("L",50),("XL",40),
          ("X",10),("IX",9),("V",5),("IV",4),("I",1)]


characters_in_file = 0
characters_optimal = 0

def from_roman(s):
    pass

def to_roman(value):
    if not isinstance(value,int):
        return ""

    res = ""

    for t in values:
        k,v = t
        while(value >= v):
            res +=k
            value -= v

    return res

with open("roman.txt","r") as fl:
    for line in fl.readlines():
        line = line.strip()
        value = 0

        i = 0
        while i < len(line):
            for t in values:
                k,v = t
                print(v)
                if line[i:].startswith(k):
                    value += v
                    i += len(k)

        print(line,to_roman(value),value)
        characters_in_file += len(line)
        characters_optimal += len(to_roman(value))

print(characters_in_file,characters_optimal,characters_in_file - characters_optimal)