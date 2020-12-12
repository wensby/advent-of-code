import sys

def move_north(value, ship, waypoint):
  waypoint[1] -= value

def move_south(value, ship, waypoint):
  waypoint[1] += value

def move_east(value, ship, waypoint):
  waypoint[0] += value

def move_west(value, ship, waypoint):
  waypoint[0] -= value

def turn_left(value, ship, waypoint):
  value = value % 360
  if value == 90:
    x_new = waypoint[1]
    y_new = -waypoint[0]
    waypoint[0] = x_new
    waypoint[1] = y_new
  else:
    turn_left(90, ship, waypoint)
    turn_left(value-90, ship, waypoint)

def turn_right(value, ship, waypoint):
  value = value % 360
  if value == 90:
    x_new = -waypoint[1]
    y_new = waypoint[0]
    waypoint[0] = x_new
    waypoint[1] = y_new
  else:
    turn_right(90, ship, waypoint)
    turn_right(value-90, ship, waypoint)

def move_forward(value, ship, waypoint):
  traveled = [(value * w) for w in waypoint]
  ship['crd'] = [ship['crd'][0] + traveled[0], ship['crd'][1] + traveled[1]]

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
  ship = {'crd': [0, 0] }
  waypoint = [10, -1]
  instructions = [(line[0], int(line[1:])) for line in input.splitlines()]
  follow_instructions(instructions, ship, waypoint)
  return manhattan_distance([0, 0], ship['crd'])

def follow_instructions(instructions, ship, waypoint):
  for instruction in instructions:
    follow_instruction(instruction, ship, waypoint)

def follow_instruction(instruction, ship, waypoint):
  instruction_functions[instruction[0]](instruction[1], ship, waypoint)

def manhattan_distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

if __name__ == '__main__':
  print(run(sys.stdin.read()))
