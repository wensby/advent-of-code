import sys

def move_north(value, ship):
  x, y = ship['crd']
  ship['crd'] = [x, y-value]

def move_south(value, ship):
  x, y = ship['crd']
  ship['crd'] = [x, y+value]

def move_east(value, ship):
  x, y = ship['crd']
  ship['crd'] = [x+value, y]

def move_west(value, ship):
  x, y = ship['crd']
  ship['crd'] = [x-value, y]

def turn_left(value, ship):
  value = value % 360
  if value == 90:
    if ship['dir'] == 'N':
      ship['dir'] = 'W'
    elif ship['dir'] == 'W':
      ship['dir'] = 'S'
    elif ship['dir'] == 'S':
      ship['dir'] = 'E'
    else:
      ship['dir'] = 'N'
  else:
    turn_left(90, ship)
    turn_left(value-90, ship)

def turn_right(value, ship):
  value = value % 360
  if value == 90:
    if ship['dir'] == 'N':
      ship['dir'] = 'E'
    elif ship['dir'] == 'E':
      ship['dir'] = 'S'
    elif ship['dir'] == 'S':
      ship['dir'] = 'W'
    else:
      ship['dir'] = 'N'
  else:
    turn_right(90, ship)
    turn_right(value-90, ship)

def move_forward(value, ship):
  if ship['dir'] == 'N':
    move_north(value, ship)
  elif ship['dir'] == 'W':
    move_west(value, ship)
  elif ship['dir'] == 'S':
    move_south(value, ship)
  else:
    move_east(value, ship)

instruction_functions = {
  'N': move_north,
  'S': move_south,
  'E': move_east,
  'W': move_west,
  'L': turn_left,
  'R': turn_right,
  'F': move_forward
}

def run(input):
  ship = {'crd': [0, 0], 'dir': 'E'}
  instructions = [(line[0], int(line[1:])) for line in input.splitlines()]
  follow_instructions(instructions, ship)
  return manhattan_distance([0, 0], ship['crd'])

def follow_instructions(instructions, ship):
  for instruction in instructions:
    follow_instruction(instruction, ship)

def follow_instruction(instruction, ship):
  instruction_functions[instruction[0]](instruction[1], ship)

def manhattan_distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

if __name__ == '__main__':
  print(run(sys.stdin.read()))
