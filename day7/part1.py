import sys

with open("input7.txt", "r") as f:
	all_steps = set()
	requirements = {}
	for line in f:
		parts = line.split()
		must_be_done = parts[1]
		before_this = parts[7]

		if before_this not in requirements:
			all_steps.add(must_be_done)
			all_steps.add(before_this)
			requirements[before_this] = [must_be_done]
		else:
			requirements[before_this].append(must_be_done)
	
	order = ""
	while len(requirements):
		next_step = "Z"
		
		# print(f"order: {order}, reqs: {sorted(requirements.keys())}")
		for step in all_steps:
			if step in order:
				continue
			if step not in requirements:
				if step < next_step:
					next_step = step

		order += next_step
		to_delete = []
		# print("next_step:", next_step)
		for step in requirements.keys():
			try:
				requirements[step].remove(next_step)
				if not len(requirements[step]):
					to_delete.append(step)
			except ValueError:
				pass

		for letter in to_delete:
			del requirements[letter]
			# print("deleted:", letter)

	for letter in all_steps:
		if letter not in order:
			order += letter
			break

	print("order:", order)
