import time
import sys
import os
import curses
import tty
import termios
import select

class Process:

  def __init__(self, program, input, output):
    self._program = program.copy()
    self._input = input
    self._output = output
    self._heap = {}
    self._wait_input = False
    self._halted = False
    self._instruction_ptr = 0
    self._relative_base = 0

  def run(self):
    self._wait_input = False
    while not (self._halted or self._wait_input):
      self._run_instruction()

  def halted(self):
    return self._halted

  def wait_input(self):
    return self._wait_input

  def _run_instruction(self):
    opcode = self._current_opcode()
    if opcode == 1:
      self._add()
    elif opcode == 2:
      self._mul()
    elif opcode == 3:
      self._in()
    elif opcode == 4:
      self._out()
    elif opcode == 5:
      self._if()
    elif opcode == 6:
      self._ifnot()
    elif opcode == 7:
      self._lt()
    elif opcode == 8:
      self._eq()
    elif opcode == 9:
      self._adjust_relative_base()
    elif opcode == 99:
      self._halt()

  def _add(self):
    a = self._param_read(0)
    b = self._param_read(1)
    self._param_write(2, a + b)
    self._instruction_ptr += 4

  def _mul(self):
    a = self._param_read(0)
    b = self._param_read(1)
    self._param_write(2, a * b)
    self._instruction_ptr += 4

  def _in(self):
    if len(self._input) == 0:
      self._wait_input = True
    else:
      self._param_write(0, self._input.pop())
      self._instruction_ptr += 2

  def _out(self):
    self._output.insert(0, self._param_read(0))
    self._instruction_ptr += 2

  def _if(self):
    if self._param_read(0):
      self._instruction_ptr = self._param_read(1)
    else:
      self._instruction_ptr += 3

  def _ifnot(self):
    if not self._param_read(0):
      self._instruction_ptr = self._param_read(1)
    else:
      self._instruction_ptr += 3

  def _lt(self):
    a = self._param_read(0)
    b = self._param_read(1)
    self._param_write(2, 1 if a < b else 0)
    self._instruction_ptr += 4

  def _eq(self):
    a = self._param_read(0)
    b = self._param_read(1)
    self._param_write(2, 1 if a == b else 0)
    self._instruction_ptr += 4

  def _adjust_relative_base(self):
    self._relative_base += self._param_read(0)
    self._instruction_ptr += 2

  def _halt(self):
    self._halted = True

  def _current_opcode(self):
    return self._read_memory(self._instruction_ptr) % 100

  def _param_read(self, param_index):
    param_position = self._param_position(param_index)
    param_value = self._read_memory(param_position)
    mode = self._param_mode(param_index)
    if mode == 0:
      return self._read_memory(param_value)
    elif mode == 1:
      return self._read_memory(param_position)
    elif mode == 2:
      return self._read_memory(self._relative_base + param_value)
    else:
      raise Exception(f'unexpected input param mode {mode}')

  def _param_write(self, param_index, value):
    param_position = self._param_position(param_index)
    param_value = self._read_memory(param_position)
    mode = self._param_mode(param_index)
    if mode == 0:
      self._write_memory(param_value, value)
    elif mode == 1:
      raise Exception('writing to param of mode 1')
    elif mode == 2:
      self._write_memory(self._relative_base + param_value, value)
    else:
      raise Exception(f'unexpected output param mode {mode}')

  def _param_position(self, index):
    return self._instruction_ptr + 1 + index

  def _param_mode(self, index):
    signature = self._read_memory(self._instruction_ptr) 
    mode_str = str(signature // 100).zfill(10)[::-1]
    return int(mode_str[index])

  def _read_memory(self, position):
    program_length = len(self._program)
    if position < program_length:
      return self._program[position]
    else:
      heap_position = position - program_length
      if heap_position not in self._heap:
        self._heap[heap_position] = 0
      return self._heap[heap_position]

  def _write_memory(self, position, value):
    program_length = len(self._program)
    if position < program_length:
      self._program[position] = value
    else:
      heap_position = position - program_length
      self._heap[heap_position] = value

tile_by_id = {
  0: ' ',
  1: '#',
  2: '█',
  3: '=',
  4: 'O',
}

def run(puzzle_input):
  program = parse_program(puzzle_input)
  program[0] = 2
  program_input = []
  output = []
  process = Process(program, program_input, output)
  ball_pos = (0, 0)
  ball_dir = 0
  paddle_pos = (0, 0)
  score = 0
  print('\033[?25l\033[?1049h', end='')
  while not process.halted():
    process.run()
    if len(output) > 0:
      score = update_score(output, score)
      new_pos = find_pos(output, 4)
      if new_pos is not None:
        ball_pos = new_pos
      new_paddle = find_pos(output, 3)
      if new_paddle is not None:
        paddle_pos = new_paddle
    program_input.clear()
    if process.wait_input():
      program_input.insert(0, read_joystick(ball_pos, paddle_pos))
    render(output)
  print('\033[?25h\033[?1049l', end='')
  return score

def update_score(output, score):
  reversed_output = output[::-1]
  segments = [reversed_output[x:x+3] for x in range(0,len(reversed_output),3)]
  for segment in segments:
    if len(segment) == 3 and segment[0] == -1 and segment[1] == 0:
      return segment[2]
  return score

def find_pos(output, tile_id):
  reversed_output = output[::-1]
  segments = [reversed_output[x:x+3] for x in range(0,len(reversed_output),3)]
  for segment in segments:
    if len(segment) == 3:
      if segment[2] == tile_id:
        return (segment[0], segment[1])
  return None

def read_joystick(ball_pos, paddle_pos):
  if ball_pos[0] < paddle_pos[0]:
    return -1
  elif ball_pos[0] > paddle_pos[0]:
    return 1
  return 0

def render(output):
  while len(output) >= 3:
    x = output.pop()
    y = output.pop()
    if x == -1 and y == 0:
      print('\033[1;1H', end='')
      print(output.pop())
    else:
      tile_id = output.pop()
      print(f'\033[{y+2};{x+1}H', end='')
      print(tile_by_id[tile_id])

def parse_program(input):
  return list(map(int, input.split(',')))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
