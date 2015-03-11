import csv
from pemath import is_triangle

def word_sum(word):
    return reduce(lambda a,x:a+x, (ord(c) - ord('A') + 1 for c in word))


count = 0

with csv.reader(open("words.txt")) as csvfile :
    for row in csvfile:
        for word in row:
            if is_triangle(word_sum(word)):
                count += 1

print count