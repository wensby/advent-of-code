import sys
import operator

def run(input):
  program = parse_program(input)
  program[1] = 12
  program[2] = 2
  run_program(program)
  return program[0]

def parse_program(input):
  return list(map(int, input.split(',')))

def run_program(program):
  pos = 0
  while program[pos] != 99:
    process_operation(program, pos)
    pos += 4

def process_operation(program, pos):
  opcode = program[pos]
  op = operator.add if opcode == 1 else operator.mul
  arg1 = program[program[pos+1]]
  arg2 = program[program[pos+2]]
  program[program[pos+3]] = op(arg1, arg2)

if __name__ == '__main__':
  print(run(sys.stdin.read()))
