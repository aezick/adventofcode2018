import sys

exit("didnt work?")

with open("example1.1") as f:
	line = f.readline().split()
	num_players = int(line[0])
	last_score = int(line[6])
	player_scores = {}

	# put marbles in the circle
	marbles = [0, 2, 1]
	marbles_length = 3  # track to avoid len(marbles) every time
	counter = 3  # the next marble to be placed
	current = 1  # the location of the current marble

	while True:
		if counter % 23 == 0:
			#print(f"current marble: {marbles[current]}, marbles: {marbles}")
			current_player = (counter % num_players) + 1
			points_earned = 0
			if current_player not in player_scores.keys():
				player_scores[current_player] = 0

			# calculate points
			points_earned += counter
			marble_to_remove = (current - 7) % marbles_length
			points_earned += marbles[marble_to_remove]
			marbles.pop(marble_to_remove)
			player_scores[current_player] += points_earned

			# do interation stuff
			marbles_length -= 1
			current = marble_to_remove % marbles_length
			#print(f"points earned: {points_earned}")
			#print(f"current marble: {marbles[current]}, marbles: {marbles}\n\n\n")

			# check if high score for stopping
			if points_earned == last_score:
				print(f"All done at marble {counter}")
				break
			if points_earned > 2000:
				print(f"quitting")
				break
			if 8317 in player_scores.values():
				print("scored enough?")
				break
		else:
			placement = (current + 2) % marbles_length
			marbles.insert(placement, counter)
			current = placement
			marbles_length += 1
			#print(f"current: {current}, marbles: {marbles}")

		counter += 1

# print scores
print(player_scores)
print(sorted(player_scores, key=player_scores.get, reverse=True))
