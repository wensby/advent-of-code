import sys

def run(input):
  layout = parse_layout(input)
  while True:
    layout, state_changes = apply_rules(layout)
    if not state_changes:
      break
  return calc_occupied_seats(layout)

def parse_layout(input):
  return [line for line in input.splitlines()]

def apply_rules(layout):
  state_changes = 0
  new_layout = []
  for row in range(0, len(layout)):
    new_row = []
    for col in range(0, len(layout[row])):
      new_state = get_new_state(layout, row, col)
      if new_state != layout[row][col]:
        state_changes += 1
      new_row.append(new_state)
    new_layout.append(''.join(new_row))
  return new_layout, state_changes

def get_new_state(layout, row, col):
  current = layout[row][col]
  if current == '.':
    return '.'
  elif current == 'L':
    return 'L' if occupied_adjacent(layout, row, col) else '#'
  else:
    return 'L' if four_or_more_neighbours(layout, row, col) else '#'

def calc_occupied_seats(layout):
  return sum(row.count('#') for row in layout)

def occupied_adjacent(layout, row, col):
  for adjacent in adjacents(layout, row, col):
    if adjacent == '#':
      return True
  return False

def four_or_more_neighbours(layout, row, col):
  count_occupied = 0
  for adjacent in adjacents(layout, row, col):
    if adjacent == '#':
      count_occupied += 1
  return count_occupied >= 4


def adjacents(layout, row, col):
  width = len(layout[0])
  height = len(layout)
  first_row = row == 0
  if not first_row:
    yield layout[row-1][col]
  first_col = col == 0
  if not first_col:
    yield layout[row][col-1]
  if not (first_row or first_col):
    yield layout[row-1][col-1]
  last_row = row == height-1
  if not last_row:
    yield layout[row+1][col]
  last_col = col == width-1
  if not last_col:
    yield layout[row][col+1]
  if not (last_row or last_col):
    yield layout[row+1][col+1]
  if not (first_row or last_col):
    yield layout[row-1][col+1]
  if not (last_row or first_col):
    yield layout[row+1][col-1]

if __name__ == '__main__':
  print(run(sys.stdin.read()))
