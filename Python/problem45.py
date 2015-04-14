from pemath import hexagonal_numbers, is_pentagonal

for hexa in hexagonal_numbers():
	
	if hexa > 40755 and is_pentagonal(hexa):
		print hexa
		break