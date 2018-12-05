import sys

twos = 0
threes = 0

with open("input2.txt", "r") as f:
	for line in f:
		twos_found = 0
		threes_found = 0
		d = {}

		for c in line.strip():
			if c in d:
				if d[c] == 1:
					twos_found += 1
					d[c] += 1
				elif d[c] == 2:
					twos_found -= 1
					threes_found += 1
					d[c] += 1
				elif d[c] == 3:
					threes_found -= 1
					d[c] += 1
			else:
				d[c] = 1

		if twos_found > 0:
			twos += 1
		if threes_found > 0:
			threes += 1

print(f"twos: {twos}, threes: {threes}, math: {twos * threes}")
