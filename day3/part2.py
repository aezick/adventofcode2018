import sys

# set of pairs, x to y
# d = {"23,45" : "claim#"}

with open("input3.txt", "r") as f:
	cloth = {}
	count = 0
	
	pures = set()
	bads = set()

	for line in f:
		parts = line.split()
		claim = int(parts[0][1:])
		key = parts[2][:-1]
		start_x, start_y = key.split(",")
		wide, tall = parts[3].split("x")

		start_x = int(start_x)
		start_y = int(start_y)
		wide = int(wide)
		tall = int(tall)

		current_x = start_x
		current_y = start_y

		max_x = start_x + wide # less than this
		max_y = start_y + tall

		while current_x < max_x:
			while current_y < max_y:
				loc = str(current_x) + "," + str(current_y)
				if loc not in cloth:
					cloth[loc] = claim
					pures.add(claim)
				elif cloth[loc] is not "X":
					bads.add(cloth[loc])
					cloth[loc] = "X"
					count += 1
					bads.add(claim)
				current_y += 1
			current_x += 1
			current_y = start_y

	print("Count:", count)
	for p in pures:
		if p not in bads:
			print(p)
