import collections
import sys

class Fighter:
	def __init__(self, x_in, y_in, race_in):
		self.impassable = ["#", "E", "G"]
		self.races = ["E", "G"]

		# x, y, race, health
		self.x = x_in
		self.y = y_in
		self.race = race_in
		self.enemy = "E" if race_in == "G" else "G"
		self.hp = 200
		self.attack_power = 3

		if self.race not in self.races:
			raise Exception("invalid race")

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return f"{self.race}: ({self.x}, {self.y}) {self.hp} hp"

	def act(self, grid, fighters):
		# return None or fighter to attack
		target = self.is_next_to_enemy(self.get_pos(), grid, fighters)
		if not target:
			next_space = self.move(grid, fighters)
			if next_space == None:
				raise ValueError(f"Nowhere to move: {target}, {self.get_pos()}")

			grid[self.y][self.x] = "."
			self.x = next_space[0]
			self.y = next_space[1]
			grid[self.y][self.x] = self.race

		target = self.is_next_to_enemy(self.get_pos(), grid, fighters)
		return target

	def move(self, grid, fighters):
		# return the space to move to

		# find closest enemies via breadth first search
		visited, q = {}, collections.deque([(self.x, self.y)])
		visited[(self.x, self.y)] = (-1, -1)
		in_range = []

		while True:
			try:
				loc = q.popleft()
			except:
				break

			points = [
				(loc[0], loc[1] - 1),
				(loc[0] - 1, loc[1]),
				(loc[0] + 1, loc[1]),
				(loc[0], loc[1] + 1)
			]

			for p in points:
				if p not in visited and grid[p[1]][p[0]] != "#":
					visited[p] = loc

					target = self.is_next_to_enemy(p, grid, fighters)
					if target and p not in in_range:
						in_range.append(p)
					else:
						q.append(p)
		
		# print(in_range)

		# find the closest viable space
		min_dist, dest = 100000, None
		for p in in_range:
			d = 0
			current = p
			parent = None
			
			while True:
				parent = visited[current]
				if parent == (self.x, self.y):
					break
				current = parent
				d += 1

			# print(parent, p, current)

			if d < min_dist and grid[current[1]][current[0]] not in self.impassable:
				min_dist = d
				dest = current

			elif d == min_dist and (current[1] < dest[1] or \
					(current[1] == dest[1] and current[0] < dest[0])) \
					and grid[current[1]][current[0]] not in self.impassable:
				min_dist = d
				dest = current

		return dest

	def is_next_to_enemy(self, point, grid, fighters):
		# if neighboring enemy, return its position, else None
		pos = (point[0], point[1] - 1)
		enemy = None
		enemy_hp = 201

		if grid[pos[1]][pos[0]] == self.enemy:
			for f in fighters:
				if f.x == pos[0] and f.y == pos[1] and f.hp < enemy_hp:
					enemy = pos
					enemy_hp = f.hp
					break

		pos = (point[0] - 1, point[1])
		if grid[pos[1]][pos[0]] == self.enemy:
			for f in fighters:
				if f.x == pos[0] and f.y == pos[1] and f.hp < enemy_hp:
					enemy = pos
					enemy_hp = f.hp
					break

		pos = (point[0] + 1, point[1])
		if grid[pos[1]][pos[0]] == self.enemy:
			for f in fighters:
				if f.x == pos[0] and f.y == pos[1] and f.hp < enemy_hp:
					enemy = pos
					enemy_hp = f.hp
					break

		pos = (point[0], point[1] + 1)
		if grid[pos[1]][pos[0]] == self.enemy:
			for f in fighters:
				if f.x == pos[0] and f.y == pos[1] and f.hp < enemy_hp:
					enemy = pos
					enemy_hp = f.hp
					break

		return enemy

	def get_pos(self):
		return (self.x, self.y)

def main():
	with open("example1") as f:
		dim_x = dim_y = 0
		fighters = []
		grid = []

		# setup grid
		for line in f:
			line = line[:-1]  # strip newline
			grid.append(list(line))

			# set dimensions of the combat
			if not dim_x:
				dim_x = len(line)
			
			# add fighters
			x_pos = 0
			for c in line:
				if c == "E":
					elf = Fighter(x_pos, dim_y, "E")  # x, y, race, health
					fighters.append(elf)
				if c == "G":
					goblin = Fighter(x_pos, dim_y, "G")
					fighters.append(goblin)

				x_pos += 1
			dim_y += 1
		
		# start fighting
		round_num = 0

		print(round_num)
		print(fighters)
		for line in grid:
			print("".join(line))

		while True:
			try:
				to_remove = []
				for f in fighters:
					if f.hp > 0:
						target = f.act(grid, fighters)

						if target:  # find fighter and reduce hp
							for t in fighters:
								if t.x == target[0] and t.y == target[1]:
									t.hp -= f.attack_power

									if t.hp <= 0:  # are they dead now?
										grid[t.y][t.x] = "."
									break
				# end for

				round_num += 1
				print(round_num)
				print(fighters)
				for line in grid:
					print("".join(line))

				input()

			except StopIteration as e:
				break
		# end while
		
		print("round_num:", round_num)
		total_hp_remaining = 0
		for f in fighters:
			total_hp_remaining += f.hp

		print("Total hp:", total_hp_remaining, fighters)
		for line in grid:
			print("".join(line))

if __name__ == "__main__":
	main()