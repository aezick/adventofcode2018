import numpy as np
import sys

def calculate_power(x, y):
	rack_id = x + 10  # variable names based on instructions
	start_with = rack_id * y
	increase = start_with + 2694  # grid serial id
	set_the_power = increase * rack_id

	try:
		third_digit = int(str(set_the_power)[-3])
	except:
		third_digit = 0
	return third_digit - 5

def main():
	grid = np.zeros((300, 300))

	for x in range(300):
		for y in range(300):
			grid[x][y] = calculate_power(x, y)

	# now find the most powerful 3x3 grid
	max_sum = -30
	saved_coordinates = ""
	for x in range(297):
		for y in range(297):
			inner_sum = 0
			for inner_x in range(0,3):
				for inner_y in range(0,3):
					inner_sum += grid[x + inner_x][y + inner_y]
			if inner_sum > max_sum:
				saved_coordinates = f"{x},{y}"
				max_sum = inner_sum
	
	print("coordinates:", saved_coordinates)


if __name__ == "__main__":
	main()
