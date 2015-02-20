import operator


def digitSum(n):
    return reduce(operator.add,(int(c) for c in str(n)))

maxSum = 0
for a in range(90,101):
    for b in range(90,101):
        maxSum = max(maxSum,digitSum(a**b))

print maxSum