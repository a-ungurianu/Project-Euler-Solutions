
triangle = []

for line in open("input.txt"):
	triangle.append([int(s) for s in line.split()])

for i in range(1,len(triangle)):
	triangle[i][0] += triangle[i-1][0]
	triangle[i][len(triangle[i])-1] += triangle[i-1][len(triangle[i-1])-1]
	for j in range(1,len(triangle[i])-1):
		triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])

print max(triangle[len(triangle)-1])
