import sys

f = open("input8.txt")

inputs = f.read().split()

idx = total = 0

def read_child():
	# ewwwwwwwwww
	global idx
	value = 0

	children = int(inputs[idx])
	metadata = int(inputs[idx + 1])
	child_values = {}
	idx += 2

	c = m = 0

	while c < children:
		child_values[c] = read_child()
		c += 1

	if children == 0:
		while m < metadata:
			value += int(inputs[idx])
			m += 1
			idx += 1
	else:
		while m < metadata:
			child_to_add = int(inputs[idx])
			try:
				value += child_values[child_to_add - 1]
			except:
				pass
			m += 1
			idx += 1

	return value

# and run the thing
total = read_child()
print(total)
