import sys
from time import sleep

result = 0
iterations = 0
values = []

while True:
	with open("input1.txt", "rb") as f:
		for val in f:
			val = int(val)
			result += val
			if result in values:
				print(result)
				exit()
			else:
				values.append(result)
				# print(sorted(values))
				# sleep(1)

	iterations += 1
	# print(f"Iteration {iterations}")

	if iterations == 250:
		for v in sorted(values):
			print(v)
		exit()
