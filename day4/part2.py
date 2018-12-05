import sys

# [1518-11-21 00:00] Guard #1471 begins shift

with open("input4.txt", "r") as f:
	d = {}
	minutes = {}
	sleep_start = 0
	most = 0
	most_id = ""
	guard_id = ""

	for line in f:
		parts = line[1:].split()
		date = parts[0]
		time = parts[1][:-1]
		temp_str = parts[3]

		if temp_str == "asleep":
			sleep_start = time
		elif temp_str == "up":
			hour, minute = sleep_start.split(":")
			end_hour, end_minute = time.split(":")

			hour = int(hour)
			minute = int(minute)
			end_hour = int(end_hour)
			end_minute = int(end_minute)

			d[guard_id] += end_minute - minute
			if d[guard_id] > most:
				most = d[guard_id]
				most_id = guard_id

			while end_minute > minute:
				if minute not in minutes:
					minutes[minute] = [guard_id]
				else:
					minutes[minute].append(guard_id)
				minute += 1

		else:
			guard_id = temp_str
			if guard_id not in d:
				d[guard_id] = 0

	max_min = 0
	max_id = ""
	max_min_min = -1
	for m in minutes:
		count = {}
		for c in minutes[m]:
			if c not in count:
				count[c] = 0
			count[c] += 1

		most = max(count, key=count.get)
		
		print(f"minute: {m}, most: {most}")
		# print(max(count, key=count.get))
		# print(count[most])

		if count[most] > max_min:
			max_min = count[most]
			max_id = most
			max_min_min = m

	print("id:", max_id, "min:", max_min_min)
