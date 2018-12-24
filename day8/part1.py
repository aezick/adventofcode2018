import sys

f = open("input8.txt")

inputs = f.read().split()

idx = total = 0

def read_child():
	# ewwwwwwwwww
	global idx
	global total

	children = int(inputs[idx])
	metadata = int(inputs[idx + 1])
	idx += 2

	c = m = 0

	while c < children:
		read_child()
		c += 1

	while m < metadata:
		total += int(inputs[idx])
		m += 1
		idx += 1

# and run the stuff
read_child()
print("total:", total)
