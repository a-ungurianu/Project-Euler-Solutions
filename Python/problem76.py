from functools import lru_cache

@lru_cache(maxsize=100000)
def _p(n,m):
    if n <= 1:
        return 1

    if m > n:
        return _p(n,n)

    partition_count = 0
    for k in range(1,m+1):
        partition_count += _p(n-k,k)

    return partition_count

def p(n):
    return _p(n,n)

print(p(100) - 1) # -1 because 100 = 100 isn't consider a summation in this probeem