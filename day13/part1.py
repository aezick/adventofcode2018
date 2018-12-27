import sys
from operator import itemgetter

with open("input13.txt") as f:
	grid = []
	y = 0  # positions
	valid_carts = ["^",">","v","<"]
	turn_order = ["L","S","R"]
	carts = []	# add tuples with (x,y,direction,next turn)
	for line in f:
		grid.append(line.strip("\n"))
		
		x = 0
		for c in line:
			if c in valid_carts:
				carts.append([x, y, c, "L"])
			x += 1
		y += 1

	counter = 0
	# print(carts)

	while True:
		carts = sorted(carts, key=itemgetter(0))
		# print(carts)

		for idx in range(0, len(carts)):
			# check for crashes
			cart_locs = []
			# print(idx, carts[idx])

			for i in range(0, len(carts)):
				loc = (carts[i][0], carts[i][1])
				if loc in cart_locs:
					print("crash:", loc)
					print(carts)
					exit()
				cart_locs.append(loc)

			# move the cart
			if carts[idx][2] == "^":
				x = carts[idx][0]
				y = carts[idx][1]
				next_space = grid[y - 1][x]
				
				if next_space == "/":
					carts[idx][2] = ">"
				elif next_space == "\\":
					carts[idx][2] = "<"
				elif next_space == "+":
					if carts[idx][3] == "L":
						carts[idx][2] = "<"
						carts[idx][3] = "S"
					elif carts[idx][3] == "S":
						carts[idx][3] = "R"
					elif carts[idx][3] == "R":
						carts[idx][2] = ">"
						carts[idx][3] = "L"
				elif next_space == " ":
					exit("^ space")

				carts[idx][1] = carts[idx][1] - 1

			elif carts[idx][2] == ">":
				x = carts[idx][0]
				y = carts[idx][1]
				next_space = grid[y][x + 1]
				
				if next_space == "/":
					carts[idx][2] = "^"
				elif next_space == "\\":
					carts[idx][2] = "v"
				elif next_space == "+":
					if carts[idx][3] == "L":
						carts[idx][2] = "^"
						carts[idx][3] = "S"
					elif carts[idx][3] == "S":
						carts[idx][3] = "R"
					elif carts[idx][3] == "R":
						carts[idx][2] = "v"
						carts[idx][3] = "L"
					elif next_space == " ":
						exit("> space")

				carts[idx][0] = carts[idx][0] + 1

			elif carts[idx][2] == "v":
				x = carts[idx][0]
				y = carts[idx][1]
				next_space = grid[y + 1][x]
				
				if next_space == "/":
					carts[idx][2] = "<"
				elif next_space == "\\":
					carts[idx][2] = ">"
				elif next_space == "+":
					if carts[idx][3] == "L":
						carts[idx][2] = ">"
						carts[idx][3] = "S"
					elif carts[idx][3] == "S":
						carts[idx][3] = "R"
					elif carts[idx][3] == "R":
						carts[idx][2] = "<"
						carts[idx][3] = "L"
					elif next_space == " ":
						exit("v space")

				carts[idx][1] = carts[idx][1] + 1

			elif carts[idx][2] == "<":
				x = carts[idx][0]
				y = carts[idx][1]
				next_space = grid[y][x - 1]
				
				if next_space == "/":
					carts[idx][2] = "v"
				elif next_space == "\\":
					carts[idx][2] = "^"
				elif next_space == "+":
					if carts[idx][3] == "L":
						carts[idx][2] = "v"
						carts[idx][3] = "S"
					elif carts[idx][3] == "S":
						carts[idx][3] = "R"
					elif carts[idx][3] == "R":
						carts[idx][2] = "^"
						carts[idx][3] = "L"
					elif next_space == " ":
						exit("< space")

				carts[idx][0] = carts[idx][0] - 1
		# end movement for loop
		counter += 1
