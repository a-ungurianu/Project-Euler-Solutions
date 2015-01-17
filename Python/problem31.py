
pos = [0]*201

pos[0] = 1

def addCoin(coin) :
	for i in range(0,201-coin):
		pos[i+coin] += pos[i]

addCoin(1)
addCoin(2)
addCoin(5)
addCoin(10)
addCoin(20)
addCoin(50)
addCoin(100)
addCoin(200)

print pos[200]
