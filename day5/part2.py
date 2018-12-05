import sys
from string import ascii_lowercase

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

	part1_line = line
	print(len(line.strip())
	min_line = len(part1_line)
	min_letter = ""

	for letter in ascii_lowercase:
		line = part1_line.replace(letter, "").replace(letter.upper(), "")
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
		
		if len(line) < min_line:
			min_line = len(line.strip())
			min_letter = letter

	
	print("min:", min_line)
	print("min letter:", min_letter)
