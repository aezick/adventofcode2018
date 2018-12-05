import sys

with open("input5.txt", "r") as f:
	line = f.readline()
	found_match = True

	while found_match:
		found_match = False
		prev = ""
		s = ""

		for c in line:
			s += c
			#print(f"prev: {prev}, c: {c}, s: {s}")
			if prev.upper() == c and prev != c:
				found_match = True
				s = s[:-2]
				prev = "-"
			elif prev.lower() == c and prev != c:
				found_match = True
				s = s[:-2]
				prev = "-"
			else:
				prev = c
		line = s

	print(line)
	print(len(line.strip()))
