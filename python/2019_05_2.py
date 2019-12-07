import sys
import operator

class Program:

  def __init__(self, memory):
    self._memory = memory

  def run(self, input):
    output = []
    instruction_pointer = [0]
    while self._memory[instruction_pointer[0]] != 99:
      instruction = self._get_instruction(instruction_pointer[0])
      instruction.run(input, instruction_pointer, self._memory, output)
    return output[-1]

  def _get_instruction(self, position):
    instruction_signature = self._memory[position]
    opcode = instruction_signature % 100
    if opcode in [1, 2, 7, 8]:
      return Instruction(self._memory[position:position+4])
    elif opcode in [3, 4]:
      return Instruction(self._memory[position:position+2])
    elif opcode in [5, 6]:
      return Instruction(self._memory[position:position+3])

class Instruction:

  def __init__(self, values):
    self._opcode = values[0] % 100
    self._params = values[1:]
    self._param_modes = str(values[0] // 100).zfill(len(values)-1)[::-1]

  def run(self, input, instruction_pointer, memory, output):
    if self._opcode == 3:
      memory[self._params[0]] = input
      instruction_pointer[0] += 2
    elif self._opcode == 4:
      value = self._get_param_value(0, memory)
      output.append(value)
      instruction_pointer[0] += 2
    elif self._opcode in [1, 2]:
      op = operator.add if self._opcode == 1 else operator.mul
      value1 = self._get_param_value(0, memory)
      value2 = self._get_param_value(1, memory)
      memory[self._params[2]] = op(value1, value2)
      instruction_pointer[0] += 4
    elif self._opcode in [5, 6]:
      value = self._get_param_value(0, memory)
      dest = self._get_param_value(1, memory)
      jump = value != 0 if self._opcode == 5 else value == 0
      if jump:
        instruction_pointer[0] = dest
      else:
        instruction_pointer[0] += 3
    elif self._opcode in [7, 8]:
      op = operator.lt if self._opcode == 7 else operator.eq
      value1 = self._get_param_value(0, memory)
      value2 = self._get_param_value(1, memory)
      memory[self._params[2]] = 1 if op(value1, value2) else 0
      instruction_pointer[0] += 4
    
  def _is_immediate_param(self, index):
    return self._param_modes[index] == '1'

  def _get_param_value(self, index, memory):
    if self._is_immediate_param(index):
      return self._params[index]
    return memory[self._params[index]]

def run(input):
  program = parse_program(input)
  return program.run(5)

def parse_program(input):
  return Program(list(map(int, input.split(','))))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
