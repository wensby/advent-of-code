import sys

def accumulate(instruction, process):
  process['accumulator'] += int(instruction[1])
  process['instr_ptr'] += 1

def jump(instruction, process):
  process['instr_ptr'] += int(instruction[1])

def no_op(instruction, process):
  process['instr_ptr'] += 1

instruction_fuctions = {
    'acc': accumulate,
    'jmp': jump,
    'nop': no_op
}

def run(input):
  instructions = [x.split(' ') for x in input.splitlines()]
  for i in range(0, len(instructions)):
    if instructions[i][0] in ['nop', 'jmp']:
      instructions[i][0] = 'nop' if instructions[i][0] == 'jmp' else 'jmp'
      result = run_program(instructions)
      if not result == -1:
        return result
      instructions[i][0] = 'nop' if instructions[i][0] == 'jmp' else 'jmp'
  return -1

def run_program(instructions):
  visited_addresses = set()
  process = {
      'instr_ptr': 0, 
      'accumulator': 0 
  }
  while process['instr_ptr'] not in visited_addresses:
    if process['instr_ptr'] == len(instructions):
      return process['accumulator']
    visited_addresses.add(process['instr_ptr'])
    instruction = instructions[process['instr_ptr']]
    instruction_fuctions[instruction[0]](instruction, process)
  return -1


if __name__ == '__main__':
  print(run(sys.stdin.read()))
