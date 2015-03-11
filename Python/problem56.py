from pemath import digit_sum

maxSum = 0
for a in range(90,101):
    for b in range(90,101):
        maxSum = max(maxSum,digit_sum(a**b))

print maxSum