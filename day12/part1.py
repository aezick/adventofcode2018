import sys

with open("input12.txt") as f:
	state = f.readline().split(" ")[2].strip()
	print(state)
	f.readline()
	plant_combos = []
	for line in f:
		if line[-2] == "#":
			plant_combos.append(line[0:5])

	leftmost_pot = 0
	for x in range(20):
		new_state = ""
		length = len(state)

		if state[0:2] == "##":
			new_state += "#"
			leftmost_pot -= 1

		for idx in range(0, length):
			neighbors = ""

			if idx - 2 >= 0:
				neighbors += state[idx - 2]
			else:
				neighbors += "."
			if idx - 1 >= 0:
				neighbors += state[idx - 1]
			else:
				neighbors += "."
			neighbors += state[idx]
			if idx + 1 < length:
				neighbors += state[idx + 1]
			else:
				neighbors += "."
			if idx + 2 < length:
				neighbors += state[idx + 2]
			else:
				neighbors += "."

			#print(idx, neighbors, neighbors in plant_combos)
			if neighbors in plant_combos:
				new_state += "#"
			else:
				new_state += "."

		if state[-2:] == ".#":
			new_state += "#"

		state = new_state
		print(state)

	total = 0
	for idx in range(0, len(state)):
		if state[idx] == "#":
			total += (idx + leftmost_pot)

	print("total:", total)
