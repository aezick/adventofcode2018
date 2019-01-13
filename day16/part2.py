from copy import deepcopy
import re
import sys

def addr(registers, args):
	registers[args[3]] = registers[args[1]] + registers[args[2]]
	return registers

def addi(registers, args):
	registers[args[3]] = registers[args[1]] + args[2]
	return registers

def mulr(registers, args):
	registers[args[3]] = registers[args[1]] * registers[args[2]]
	return registers

def muli(registers, args):
	registers[args[3]] = registers[args[1]] * args[2]
	return registers

def banr(registers, args):
	registers[args[3]] = registers[args[1]] & registers[args[2]]
	return registers

def bani(registers, args):
	registers[args[3]] = registers[args[1]] & args[2]
	return registers

def borr(registers, args):
	registers[args[3]] = registers[args[1]] | registers[args[2]]
	return registers

def bori(registers, args):
	registers[args[3]] = registers[args[1]] | args[2]
	return registers

def setr(registers, args):
	registers[args[3]] = registers[args[1]]
	return registers

def seti(registers, args):
	registers[args[3]] = args[1]
	return registers

def gtir(registers, args):
	registers[args[3]] = 1 if args[1] > \
		registers[args[2]] else 0
	return registers

def gtri(registers, args):
	registers[args[3]] = 1 if registers[args[1]] > args[2] else 0
	return registers

def gtrr(registers, args):
	registers[args[3]] = 1 if registers[args[1]] > \
		registers[args[2]] else 0
	return registers

def eqir(registers, args):
	registers[args[3]] = 1 if args[1] == \
		registers[args[2]] else 0
	return registers

def eqri(registers, args):
	registers[args[3]] = 1 if registers[args[1]] == args[2] else 0
	return registers

def eqrr(registers, args):
	registers[args[3]] = 1 if registers[args[1]] == \
		registers[args[2]] else 0
	return registers

def main():
	with open("input16-part2.txt") as f:
		num_of_opcodes = 16
		operations = [  # in order of number to opcode assignment
			borr,
			seti,
			mulr,
			eqri,
			banr,
			bori,
			bani,
			gtri,
			addr,
			muli,
			addi,
			eqrr,
			gtir,
			eqir,
			setr,
			gtrr
		]

		registers = [0, 0, 0, 0]

		for line in f:
			args = [int(n) for n in re.findall("\d+", line)]

			registers = operations[args[0]](registers, args)
		
		print("Registers:", registers)
			
if __name__ == "__main__":
	main()
