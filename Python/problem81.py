from functools import lru_cache

matrix = []

with open("matrix.txt","r") as file:
    for line in file.readlines():
        line = line.strip()
        matrix.append(list(map(int,line.split(","))))

@lru_cache(maxsize=80*80)
def shortest_path(n,m):
    if n == 0 and m == 0:
        return matrix[0][0]
    if n == 0:
        return matrix[n][m] + shortest_path(n,m-1)
    if m == 0:
        return matrix[n][m] + shortest_path(n-1,m)

    return matrix[n][m] + min(shortest_path(n,m-1),shortest_path(n-1,m))


print(shortest_path(79,79))