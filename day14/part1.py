import sys

count = 2  # start with 2 recipes
max =  864801 + 10 # 864801
r1 = 0
r2 = 1
recipes = [3, 7]
scores = ""

while count < max:
	new_recipe = str(recipes[r1] + recipes[r2])

	for c in new_recipe:
		recipes.append(int(c))
		count += 1
		if max - count < 10:
			scores += c

	r1 = (r1 + 1 + recipes[r1]) % len(recipes)
	r2 = (r2 + 1 + recipes[r2]) % len(recipes)

# print("r1:", r1, recipes[r1], "r2:", r2, recipes[r2])
	# print("count:", count, "new recipe:", new_recipe)

print("scores:", scores[0:10])
