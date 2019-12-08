import sys
import itertools

class Process:

  def __init__(self, program, input, output):
    self._program = program.copy()
    self._input = input
    self._output = output
    self._instruction_pointer = 0
    self._halted = False

  def run(self):
    self._awaiting_input = False
    while not self._halted and not self._awaiting_input:
      self._run_instruction()

  def halted(self):
    return self._halted

  def _run_instruction(self):
    instruction_signature = self._program[self._instruction_pointer]
    opcode = instruction_signature % 100
    if opcode == 99:
      self._halted = True
    elif opcode == 1:
      self._add()
    elif opcode == 2:
      self._mul()
    elif opcode == 3:
      self._in()
    elif opcode == 4:
      self._out()
    elif opcode == 5:
      self._if_true()
    elif opcode == 6:
      self._if_false()
    elif opcode == 7:
      self._lt()
    elif opcode == 8:
      self._eq()

  def _add(self):
    a = self._resolved_param_value(0)
    b = self._resolved_param_value(1)
    des = self._raw_param_value(2)
    self._program[des] = a + b
    self._instruction_pointer += 4

  def _mul(self):
    a = self._resolved_param_value(0)
    b = self._resolved_param_value(1)
    des = self._raw_param_value(2)
    self._program[des] = a * b
    self._instruction_pointer += 4

  def _in(self):
    if len(self._input) == 0:
      self._awaiting_input = True
    else:
      value = self._input.pop()
      des = self._raw_param_value(0)
      self._program[des] = value
      self._instruction_pointer += 2

  def _out(self):
    value = self._resolved_param_value(0)
    self._output.insert(0, value)
    self._instruction_pointer += 2

  def _if_true(self):
    if self._resolved_param_value(0):
      self._instruction_pointer = self._resolved_param_value(1)
    else:
      self._instruction_pointer += 3

  def _if_false(self):
    if not self._resolved_param_value(0):
      self._instruction_pointer = self._resolved_param_value(1)
    else:
      self._instruction_pointer += 3

  def _lt(self):
    a = self._resolved_param_value(0)
    b = self._resolved_param_value(1)
    des = self._raw_param_value(2)
    self._program[des] = 1 if a < b else 0
    self._instruction_pointer += 4

  def _eq(self):
    a = self._resolved_param_value(0)
    b = self._resolved_param_value(1)
    des = self._raw_param_value(2)
    self._program[des] = 1 if a == b else 0
    self._instruction_pointer += 4

  def _resolved_param_value(self, index):
    value = self._raw_param_value(index)
    return value if self._is_immediate_param(index) else self._program[value]

  def _is_immediate_param(self, index):
    signature = self._program[self._instruction_pointer]
    modes = str(signature)[0:-2].zfill(10)[::-1]
    return int(modes[index])

  def _raw_param_value(self, index):
    return self._program[self._instruction_pointer + index + 1]


def run(input):
  amp_program = parse_program(input)
  max_thrust = 0
  for phase_settings in list(itertools.permutations([5, 6, 7, 8, 9])):
    thrust = run_amplifiers(phase_settings, amp_program)
    max_thrust = max(thrust, max_thrust)
  return max_thrust

def parse_program(input):
  return list(map(int, input.split(',')))

def run_amplifiers(phase_settings, amp_program):
  # make input streams prefilled with amplifier settings
  ins = [[setting] for setting in phase_settings]
  processes = [Process(amp_program, ins[i], ins[(i+1)%5]) for i in range(5)]
  ins[0].insert(0, 0) # add 0 as initial input
  while not processes[4].halted():
    for i in range(5):
      processes[i].run()
  return ins[0].pop()

if __name__ == '__main__':
  print(run(sys.stdin.read()))
