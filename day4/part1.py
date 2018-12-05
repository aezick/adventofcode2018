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

			if guard_id == "#2633":
				while end_hour > hour or end_minute > minute:
					if minute not in minutes:
						minutes[minute] = 1
					else:
						minutes[minute] += 1
					minute += 1
					if minute == 60:
						minute = 00
						hour += 1

		else:
			guard_id = temp_str
			if guard_id not in d:
				d[guard_id] = 0

	print(most_id)
	print(d)

	maxx = 0
	maxx_min = -1
	for m in minutes:
		if minutes[m] > maxx:
			maxx = minutes[m]
			maxx_min = m
			print(m)

	print("real", maxx_min)
