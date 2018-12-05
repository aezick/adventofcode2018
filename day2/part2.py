import sys

with open("input2.txt", "r") as f_outer:
	for line_outer in f_outer:
		with open("input2.txt", "r") as f_inner:
			for line_inner in f_inner:
				idx = 0
				misses = 0
				limit = len(line_inner)
				while misses < 2 and idx < limit:
					if line_outer[idx] != line_inner[idx]:
						misses += 1
					idx += 1

				if misses == 1:
					print(f"outer: {line_outer.strip()}, inner: {line_inner.strip()}")
					exit()
