import sys
from collections import deque

class Process:

  def __init__(self, program, input_stream, output_stream):
    self._program = program.copy()
    self._in = input_stream
    self._out = output_stream
    self._heap = {}
    self._awaiting_input = False
    self._halted = False
    self._instruction_ptr = 0
    self._relative_base = 0
    self._instruction_method_by_opcode = {
        1: self._add,
        2: self._mul,
        3: self._read_in,
        4: self._write_out,
        5: self._if,
        6: self._ifn,
        7: self._lt,
        8: self._eq,
        9: self._rel_base,
        99: self._halt,
    }

  def run(self):
    self._awaiting_input = False
    while not (self._halted or self._awaiting_input):
      self._run_next_instruction()

  def is_halted(self):
    return self._halted

  def is_awaiting_input(self):
    return self._awaiting_input

  def _run_next_instruction(self):
    opcode = self._current_opcode()
    self._instruction_method_by_opcode[opcode]()
  
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

  def _read_in(self):
    if len(self._in) == 0:
      self._awaiting_input = True
    else:
      self._param_write(0, self._in.pop())
      self._instruction_ptr += 2

  def _write_out(self):
    self._out.insert(0, self._param_read(0))
    self._instruction_ptr += 2

  def _if(self):
    if self._param_read(0):
      self._instruction_ptr = self._param_read(1)
    else:
      self._instruction_ptr += 3

  def _ifn(self):
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

  def _rel_base(self):
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

class SectionExplorer:

  def __init__(self, droid_program):
    self._droid_program = droid_program

  def explore_section(self):
    passable_by_position = { (0, 0): True }
    droid_position = (0, 0)
    current_path = []
    goal_position = None
    process_input = []
    process_output = []
    process = Process(self._droid_program, process_input, process_output)
    while not (goal_position and droid_position == (0, 0)):
      candidate_input = self.get_candidate_input(droid_position, passable_by_position)
      if not candidate_input:
        # backtrack
        backtrack_dir = self.opposite(current_path.pop())
        droid_position = self.calc_droid_position(droid_position, backtrack_dir)
        process_input.insert(0, backtrack_dir)
        process.run()
        process_output.pop()
      else:
        next_dir = candidate_input
        next_pos = self.calc_droid_position(droid_position, next_dir)
        process_input.insert(0, next_dir)
        process.run()
        droid_output = process_output.pop()
        if droid_output == 0:
          passable_by_position[next_pos] = False
        else:
          droid_position = next_pos
          passable_by_position[droid_position] = True
          current_path.append(next_dir)
        if droid_output == 2:
          goal_position = droid_position
    return passable_by_position, goal_position
  
  def opposite(self, direction):
    if direction == 1:
      return 2
    if direction == 2:
      return 1
    if direction == 3:
      return 4
    if direction == 4:
      return 3
  
  def get_candidate_input(self, droid_position, passable_by_position):
    if (droid_position[0], droid_position[1]+1) not in passable_by_position:
      return 1
    if (droid_position[0], droid_position[1]-1) not in passable_by_position:
      return 2
    if (droid_position[0]-1, droid_position[1]) not in passable_by_position:
      return 3
    if (droid_position[0]+1, droid_position[1]) not in passable_by_position:
      return 4
    return None
  
  def calc_droid_position(self, origin, mov):
    pos = list(origin)
    if mov == 1:
      pos[1] += 1
    elif mov == 2:
      pos[1] -= 1
    elif mov == 3:
      pos[0] -= 1
    else:
      pos[0] += 1
    return tuple(pos)

class OxygenSimulation:

  def __init__(self, section):
    self._section = section

  def run(self, start):
    lacks_oxygen_by_coord = self._section.copy()
    minutes = -1
    oxygen_edges = set([start])
    while oxygen_edges:
      working_edges = list(oxygen_edges)
      oxygen_edges.clear()
      for working_edge in working_edges:
        lacks_oxygen_by_coord[working_edge] = False
      for working_edge in working_edges:
        oxygen_edges.update(self._get_oxygen_lacking_adjacents(working_edge, lacks_oxygen_by_coord))
      minutes += 1
    return minutes

  def _get_oxygen_lacking_adjacents(self, pos, lacks_oxygen_by_coord):
    adjacent_positions = [
        (pos[0], pos[1]+1),
        (pos[0], pos[1]-1),
        (pos[0]+1, pos[1]),
        (pos[0]-1, pos[1]),
    ]
    return list(filter(lambda x: lacks_oxygen_by_coord.get(x, False), adjacent_positions))

def run(input):
  program = parse_program(input)
  explorer = SectionExplorer(program)
  section, goal_pos = explorer.explore_section()
  simulation = OxygenSimulation(section)
  return simulation.run(goal_pos)

def parse_program(input):
  return list(map(int, input.split(',')))


if __name__ == '__main__':
  print(run(sys.stdin.read()))
