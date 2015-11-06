

count = 0
for b in range(1,50):
    for e in range(1,50):
        if(len(str(b**e)) == e):
            count += 1

print count