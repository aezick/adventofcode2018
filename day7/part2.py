import sys

def free_workers(workers):
	for w in workers:
		if workers[w] <= 0:
			return True
	return False

with open("test", "r") as f:
	all_steps = set()
	requirements = {}
	workers = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}
	jobs = {"1": "", "2": "", "3": "", "4": "", "5": ""}

	# setup steps
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

	# complete construction
	order = ""
	count = -1
	while len(requirements) and set(order) != all_steps:
		completed_work = []

		for w in workers:
			workers[w] -= 1
			if workers[w] <= 0:
				if jobs[w]:
					completed_work.append(jobs[w])
					order += jobs[w]
					jobs[w] = ""

		next_steps = []
		
		# print(f"order: {order}, reqs: {sorted(requirements.keys())}")
		for step in all_steps:
			if step in order: 
				continue
			if step in jobs.values():
				continue
			if step not in requirements:
				next_steps.append(step)

		next_steps = sorted(next_steps)
		to_delete = []

		for w in workers:
			if workers[w] <= 0:
				try:
					s = next_steps.pop(0)
					workers[w] = ord(s) - 4
					jobs[w] = s
				except IndexError:
					pass

		# print("next_step:", next_step)
		for l in completed_work:
			for step in requirements.keys():
				try:
					requirements[step].remove(l)
					if not len(requirements[step]):
						to_delete.append(step)
				except ValueError:
					pass

		for letter in to_delete:
			del requirements[letter]
			# print("deleted:", letter)
		
		count += 1
	# end while loop

	# for last step
	for letter in all_steps:
		if letter not in order:
			order += letter
			break

	print("order:", order)
	print("count:", count)
