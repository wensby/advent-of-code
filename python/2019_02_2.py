import sys
import operator

class Program:

  def __init__(self, memory):
    self._memory = memory.copy()
    self._instr_ptr = 0

  def run(self, noun, verb):
    self._memory[1] = noun
    self._memory[2] = verb
    while self._memory[self._instr_ptr] != 99:
      self._process_instruction()
    return self._memory[0]

  def _process_instruction(self):
    instruction = self._get_instruction()
    op = operator.add if instruction[0] == 1 else operator.mul
    arg1 = self._memory[instruction[1]]
    arg2 = self._memory[instruction[2]]
    self._memory[instruction[3]] = op(arg1, arg2)
    self._instr_ptr += len(instruction)

  def _get_instruction(self):
    ptr = self._instr_ptr
    opcode = self._memory[ptr]
    if opcode == 1 or opcode == 2:
      return self._memory[ptr:ptr+4]
    else:
      return self._memory[ptr:ptr+1]

def run(input):
  memory = parse_initial_memory(input)
  for noun in range(100):
    for verb in range(100):
      program = Program(memory)
      if program.run(noun, verb) == 19690720:
        return 100 * noun + verb

def parse_initial_memory(input):
  return list(map(int, input.split(',')))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
