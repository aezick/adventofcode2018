from copy import deepcopy
import re
import sys

def addr(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = current_regs[args[1]] + current_regs[args[2]]
	
	return 1 if current_regs == after_regs else 0

def addi(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = current_regs[args[1]] + args[2]

	return 1 if current_regs == after_regs else 0

def mulr(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = current_regs[args[1]] * current_regs[args[2]]

	return 1 if current_regs == after_regs else 0

def muli(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = current_regs[args[1]] * args[2]

	return 1 if current_regs == after_regs else 0

def banr(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = current_regs[args[1]] & current_regs[args[2]]

	return 1 if current_regs == after_regs else 0

def bani(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = current_regs[args[1]] & args[2]

	return 1 if current_regs == after_regs else 0

def borr(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = current_regs[args[1]] | current_regs[args[2]]

	return 1 if current_regs == after_regs else 0

def bori(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = current_regs[args[1]] | args[2]

	return 1 if current_regs == after_regs else 0

def setr(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = current_regs[args[1]]

	return 1 if current_regs == after_regs else 0

def seti(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = args[1]

	return 1 if current_regs == after_regs else 0

def gtir(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = 1 if args[1] > \
		current_regs[args[2]] else 0

	return 1 if current_regs == after_regs else 0

def gtri(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = 1 if current_regs[args[1]] > args[2] else 0

	return 1 if current_regs == after_regs else 0

def gtrr(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)
	
	current_regs[args[3]] = 1 if current_regs[args[1]] > \
		current_regs[args[2]] else 0

	return 1 if current_regs == after_regs else 0

def eqir(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = 1 if args[1] == \
		current_regs[args[2]] else 0

	
	return 1 if current_regs == after_regs else 0

def eqri(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)

	current_regs[args[3]] = 1 if current_regs[args[1]] == args[2] else 0

	return 1 if current_regs == after_regs else 0

def eqrr(before_regs, args, after_regs):
	current_regs = deepcopy(before_regs)
	
	current_regs[args[3]] = 1 if current_regs[args[1]] == \
		current_regs[args[2]] else 0

	return 1 if current_regs == after_regs else 0

def main():
	with open("input16.txt") as f:
		count = 0
		num_of_opcodes = 16
		operations = [
			addr, addi,
			mulr, muli,
			banr, bani,
			borr, bori,
			setr, seti,
			gtir, gtri, gtrr,
			eqir, eqri, eqrr
		]

		part = 0
		before_regs = args = after_regs = []

		for line in f:
			res = [int(n) for n in re.findall("\d+", line)]

			if line[0] == "B" and part == 0 and res: 
				# print(f"before: {res}")
				before_regs = res
				part += 1
			elif part == 1 and res:
				# print("args:", res)
				args = res
				part += 1
			elif part == 2 and res:
				# print("after:", res)
				after_regs = res
				part = 0
				
				# heavy calculation time
				correct = 0
				for i in range(num_of_opcodes):
					result = operations[i](
						before_regs, args, after_regs
					)
					# print(operations[i].__name__, result)
					correct += result

					if correct == 3: # could make faster if tracked i value
						count += 1
						break

				before_regs = args = after_regs = []
		# end for
		print("Count:", count)
			
if __name__ == "__main__":
	main()
