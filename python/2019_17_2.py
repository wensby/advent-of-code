import sys
import itertools
import re
import curses
import termios

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
    self._outputted = False

  def run(self):
    self._wait_input = False
    self._outputted = False
    while not (self._halted or self._wait_input or self._outputted):
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
    self._outputted = True
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

def run(input):
  ascii_program = list(map(int, input.split(',')))
  image = get_camera_image(ascii_program)
  movement_routine = calculate_movement_routine(image)
  collected_dust = run_vacuum_robot(ascii_program, movement_routine)
  return collected_dust

def get_camera_image(ascii_program):
  output = []
  process = Process(ascii_program, [], output)
  while not process.halted():
    process.run()
  return ''.join(map(chr, reversed(output)))

def run_vacuum_robot(ascii_program, movement_routine):
  ascii_program[0] = 2 # turn on camera
  input = convert_movement_routine_to_input(movement_routine)
  input.extend(list(map(ord, 'y\n')))
  input.reverse()
  output = []
  process = Process(ascii_program, input, output)
  print_escape_code('[?25l')
  print_escape_code('[?1049h')
  while not process.halted():
    process.run()
    if process.halted():
      break
    if len(output) > 1 and output[0] == output[1] == 10:
      print_escape_code('c')
      print_escape_code('[1;1H')
      print(''.join(map(chr, reversed(output))))
      output.clear()
  print_escape_code('[?1049l')
  print_escape_code('[?25h')
  return output.pop() # get collected dust

def print_escape_code(code):
  print(f'\033{code}', end='')

def calculate_movement_routine(image):
  rows = list(filter(lambda l: len(l) > 0, image.splitlines()))
  movement = []
  robot_pos = get_robot_position(rows)
  robot_dir = rows[robot_pos[1]][robot_pos[0]]
  visited_pos = {tuple(robot_pos)}
  next_pos = get_next(rows, robot_pos, visited_pos, robot_dir)
  while next_pos:
    new_movement, next_dir = convert_movement(robot_pos, robot_dir, next_pos)
    movement.extend(new_movement)
    visited_pos.add(next_pos)
    robot_pos = next_pos
    robot_dir = next_dir
    next_pos = get_next(rows, robot_pos, visited_pos, robot_dir)
  fixed = []
  number = 0
  for m in movement:
    if type(m) == int:
      number += m
    else:
      if number:
        fixed.append(str(number))
        number = 0
      fixed.append(m)
  if number:
    fixed.append(str(number))
  routine, a, b, c = find_routine(fixed)
  return [','.join(routine), ','.join(a), ','.join(b), ','.join(c)]

def find_routine(movements):
  for a_len in range(1, 11):
    a = movements[0:a_len]
    a_replaced = replaced(movements, a, 'A')
    a_lstripped = lstrip(a_replaced, 'A')
    for b_len in range(1, min(11, find(a_lstripped, 'A', 11)+1)):
      b = a_lstripped[0:b_len]
      ab_replaced = replaced(a_replaced, b, 'B')
      ab_lstripped = lstrip(lstrip(ab_replaced, 'A'), 'B')
      for c_len in range(1, min(11, min(find(ab_lstripped,'A', 11), find(ab_lstripped, 'B', 11))+1)):
        c = ab_lstripped[0:c_len]
        abc_replaced = replaced(ab_replaced, c, 'C')
        if re.match('^[ABC]*$', ''.join(abc_replaced)):
          return abc_replaced, a, b, c

def find(subject_list, elem, default):
  try:
    return subject_list.index(elem)
  except:
    return default

def replaced(subject_list, sublist, replacement):
  result = []
  i = 0
  while i < len(subject_list):
    if len(subject_list) - i >= len(sublist) and subject_list[i:i+len(sublist)] == sublist:
      if replacement:
        result.append(replacement)
      i += len(sublist)
    else:
      result.append(subject_list[i])
      i += 1
  return result

def lstrip(subject_list, elem):
  result = subject_list.copy()
  while result[0] == elem:
    del result[0]
  return result

def convert_movement(robot_pos, robot_dir, next_pos):
  rx, ry = robot_pos
  nx, ny = next_pos
  if robot_dir == '^':
    if ny < ry:
      return [1], '^'
    elif nx < rx:
      return ['L', 1], '<'
    else:
      return ['R', 1], '>'
  elif robot_dir == 'v':
    if ny > ry:
      return [1], 'v'
    elif nx < rx:
      return ['R', 1], '<'
    else:
      return ['L', 1], '>'
  elif robot_dir == '>':
    if nx > rx:
      return [1], '>'
    elif ny < ry:
      return ['L', 1], '^'
    else:
      return ['R', 1], 'v'
  else:
    if nx < rx:
      return [1], '<'
    elif ny < ry:
      return ['R', 1], '^'
    else:
      return ['L', 1], 'v'

def get_next(rows, robot_pos, visited_pos, robot_dir):
  rx, ry = robot_pos
  left = ((rx-1, ry), rows[ry][rx-1] if rx > 0 else None)
  right = ((rx+1, ry), rows[ry][rx+1] if rx < len(rows[ry])-1 else None)
  up = ((rx, ry-1), rows[ry-1][rx] if ry > 0 else None)
  down = ((rx, ry+1), rows[ry+1][rx] if ry < len(rows)-1 else None)
  if left[1] == right[1] == up[1] == down[1] == '#': # in intersection
    # continue direction
    if robot_dir == '>':
      return right[0]
    if robot_dir == '<':
      return left[0]
    if robot_dir == '^':
      return up[0]
    if robot_dir == 'v':
      return down[0]
  else:
    if right[1] == '#' and (right[0] not in visited_pos or robot_dir == '>'):
      return right[0]
    if left[1] == '#' and (left[0] not in visited_pos or robot_dir == '<'):
      return left[0]
    if up[1] == '#' and (up[0] not in visited_pos or robot_dir == '^'):
      return up[0]
    if down[1] == '#' and (down[0] not in visited_pos or robot_dir == 'v'):
      return down[0]

def get_robot_position(rows):
  for y in range(len(rows)):
    for x in range(len(rows[y])):
      if rows[y][x] in '><v^':
        return (x, y)

def convert_movement_routine_to_input(movement_routine):
  return list(itertools.chain(*map(convert_to_ascii, movement_routine)))

def convert_to_ascii(row):
  return list(map(ord, row + '\n'))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
