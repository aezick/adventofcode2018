import sys
from string import ascii_lowercase
import itertools

# from https://stackoverflow.com/a/29351603/2521402
def iter_all_strings():
	for size in itertools.count(1):
		for s in itertools.product(ascii_lowercase, repeat=size):
			yield "".join(s)

def get_xy(loc_str):
	x,y = loc_str.strip().split(",")
	y = y.strip()
	return x,y


# make list of all starting locations
# set max bounds of map from max,min x,y of locations
# init 2d map of spaces, fill in starting locations {"coordinate": "LOC"}
# iterate around each LOC, fill in {"coordinate": "loc+Round"} while
#	also tracking the size of each LOC
# e.g. {"123,456": "AB2"}, so 123,456 is 2 dist from AB

with open("input6.txt", "r") as f:
	it = iter_all_strings()
	locs = {}
	the_map = {}
	sizes = {}
	min_x = min_y = 10000
	max_x = max_y = -1

	for line in f:
		c = next(it)
		x,y = get_xy(line)

		# set map limits
		if min_x > int(x):
			min_x = int(x)
		if min_y > int(y):
			min_y = int(y)
		if max_x < int(x):
			max_x = int(x)
		if max_y < int(y):
			max_y = int(y)

		sizes[c] = 1
		locs[c] = x + "," + y
		the_map[locs[c]] = c.upper()

	dist = 1
	some_not_oob = True  # oob = out of bounds aka infinite space

	while some_not_oob:
		some_not_oob = False

		for loc in locs:
			x,y = get_xy(locs[loc])
			x = int(x)
			y = int(y)
			walk_x = -dist
			walk_y = 0

#			for s in sizes:
#				if sizes[s] > 1:
#					print(dist, s, sizes[s])

			while walk_x <= dist:
				new_x = x + walk_x
				new_y = y + walk_y

				new_loc = str(new_x) + "," + str(new_y)

				if new_loc not in the_map:
					the_map[new_loc] = loc + "," + str(dist)
					sizes[loc] += 1
					
				elif the_map[new_loc] == ".":
					pass
				else:
					if "," in the_map[new_loc]:
						loc_id, claim = the_map[new_loc].split(",")
						if int(claim) == dist:  # if contested
							the_map[new_loc] = "."
							sizes[loc_id] -= 1

					if not some_not_oob or new_x <= min_x or \
						new_x >= max_x or new_y <= min_y or \
						new_y >= max_y:
						sizes[loc] = -1234567
					else:
						some_not_oob = True


				walk_x += 1
				walk_y += 1

				if walk_y > dist:  # reset to bottommost coor
					walk_y = -dist
					walk_x = 0

		dist += 1
	
	print("sizes:")
	print(sizes)
	print(sorted(sizes, key=sizes.get))

