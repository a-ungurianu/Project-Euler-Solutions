import csv
import math

def word_sum(word):
    return reduce(lambda a,x:a+x, (ord(c) - ord('A') + 1 for c in word))

def is_triangle(t):
    n = (math.sqrt(1 + 4*2*t) - 1) / 2
    return n == int(n)

count = 0

with csv.reader(open("words.txt")) as csvfile :
    for row in csvfile:
        for word in row:
            if is_triangle(word_sum(word)):
                count += 1

print count