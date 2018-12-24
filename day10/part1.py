import re
import sys
import matplotlib.pyplot as plt
from array import array

with open("input10.txt") as f:
	points = []
	vees = []  # velocities
	regex = r"(-?\d+)"
	counter = 0

	for line in f:
		matches = re.findall(regex, line)
		points.append((int(matches[0]), int(matches[1])))
		vees.append((int(matches[2]), int(matches[3])))
	
	while True:
		ready = True
		for idx in range(len(points)):
			points[idx] = (points[idx][0] + vees[idx][0], \
						   points[idx][1] + vees[idx][1])
			if ready:
				if points[idx][0] > 300 or points[idx][0] < 100 \
					or points[idx][1] > 300 or points[idx][1] < 100:
					ready = False

		if ready:
			x = array('l')
			y = array('l')
			max_x = 0
			max_y = 0
			for p in points:
				x.append(p[0])
				y.append(p[1])
				if abs(p[0]) > max_x:
					max_x = abs(p[0])
				if abs(p[1]) > max_y:
					max_y = abs(p[1])

			area = (max_x + 1) * (max_y + 1)
			ans = "y"
			scat = plt.scatter(x, y)
			plt.savefig(f"{counter}.png")
			scat.remove()

			if counter % 5 == 0:
				ans = input("Continue? press y")
			if ans != "y":
				exit()
			counter += 1


