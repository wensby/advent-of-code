import sys
import itertools

class Program:

  def __init__(self, program):
    self._program = program

  def run(self, input, output):
    Process(self._program, input, output).run()

class Process:

  def __init__(self, program, input, output):
    self._program = program.copy()
    self._input = input
    self._output = output
    self._instruction_pointer = 0

  def run(self):
    while self._program[self._instruction_pointer] != 99:
      self._run_instruction()

  def _run_instruction(self):
    instruction_signature = self._program[self._instruction_pointer]
    opcode = instruction_signature % 100
    if opcode == 1:
      self._add()
    elif opcode == 2:
      self._mul()
    elif opcode == 3:
      self._in()
    elif opcode == 4:
      self._out()
    elif opcode == 5:
      self._jumpiftrue()
    elif opcode == 6:
      self._jumpiffalse()
    elif opcode == 7:
      self._lt()
    elif opcode == 8:
      self._eq()

  def _add(self):
    a = self._param(0)
    b = self._param(1)
    des = self._raw_param(2)
    self._program[des] = a + b
    self._instruction_pointer += 4

  def _mul(self):
    a = self._param(0)
    b = self._param(1)
    des = self._raw_param(2)
    self._program[des] = a * b
    self._instruction_pointer += 4

  def _in(self):
    value = self._input.pop()
    des = self._raw_param(0)
    self._program[des] = value
    self._instruction_pointer += 2

  def _out(self):
    value = self._param(0)
    self._output.insert(0, value)
    self._instruction_pointer += 2

  def _jumpiftrue(self):
    if self._param(0):
      self._instruction_pointer = self._param(1)
    else:
      self._instruction_pointer += 3

  def _jumpiffalse(self):
    if not self._param(0):
      self._instruction_pointer = self._param(1)
    else:
      self._instruction_pointer += 3

  def _lt(self):
    a = self._param(0)
    b = self._param(1)
    des = self._raw_param(2)
    self._program[des] = 1 if a < b else 0
    self._instruction_pointer += 4

  def _eq(self):
    a = self._param(0)
    b = self._param(1)
    des = self._raw_param(2)
    self._program[des] = 1 if a == b else 0
    self._instruction_pointer += 4

  def _raw_param(self, index):
    return self._program[self._instruction_pointer + index + 1]

  def _param(self, index):
    signature = self._program[self._instruction_pointer]
    modes = str(signature)[0:-2].zfill(10)[::-1]
    param_pointer = self._instruction_pointer + index + 1
    param_value = self._program[param_pointer]
    if modes[index] == '1':
      return param_value
    return self._program[param_value]


def run(input):
  amplifier_program = parse_program(input)
  max_thruster = 0
  for phase_settings in list(itertools.permutations([0, 1, 2, 3, 4])):
    thruster = run_amplifiers(phase_settings, amplifier_program)
    max_thruster = max(thruster, max_thruster)
  return max_thruster

def parse_program(input):
  return Program(list(map(int, input.split(','))))

def run_amplifiers(phase_settings, amplifier_program):
  output = [0]
  for i in range(5):
    input = [output.pop(), phase_settings[i]]
    amplifier_program.run(input, output)
  return output.pop()

if __name__ == '__main__':
  print(run(sys.stdin.read()))
