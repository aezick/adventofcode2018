import sys

count = 2  # start with 2 recipes
pattern =  "864801"
idx = 0
r1 = 0
r2 = 1
recipes = [3, 7]
scores = ""

while count < 100000000:  # kept adding zeros while testing
	new_recipe = str(recipes[r1] + recipes[r2])

	for c in new_recipe:
		recipes.append(int(c))
		count += 1

		if c == pattern[idx]: 
			idx += 1
		else:
			idx = 0
		if idx == len(pattern):
			print("count:", count - len(pattern))
			exit()

	r1 = (r1 + 1 + recipes[r1]) % len(recipes)
	r2 = (r2 + 1 + recipes[r2]) % len(recipes)

