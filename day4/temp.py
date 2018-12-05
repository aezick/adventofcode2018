import sys

# [1518-11-21 00:00] Guard #1471 begins shift

with open("input4.txt", "r") as f:
	d = {}
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

		else:
			guard_id = temp_str
			d[guard_id] = 0

