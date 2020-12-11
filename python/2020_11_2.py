import sys

def run(input):
  layout = parse_layout(input)
  sighted_seats_by_seat = parse_sighted_seats_by_seat(layout)
  while True:
    layout, state_changes = apply_rules(layout, sighted_seats_by_seat)
    if not state_changes:
      break
  return calc_occupied_seats(layout)

def print_layout(layout):
  for row in layout:
    print(row)
  print()

def parse_layout(input):
  return [line for line in input.splitlines()]

def parse_sighted_seats_by_seat(layout):
  result = {}
  for x in range(0, len(layout[0])):
    result[x] = {}
    for y in range(0, len(layout)):
      result[x][y] = parse_sighted_seats(layout, x, y)
  return result

def parse_sighted_seats(layout, x, y):
  return list(adjacents(layout, y, x))

def apply_rules(layout, sighted_seats_by_seat):
  state_changes = 0
  new_layout = []
  for row in range(0, len(layout)):
    new_row = []
    for col in range(0, len(layout[row])):
      new_state = get_new_state(layout, row, col, sighted_seats_by_seat)
      if new_state != layout[row][col]:
        state_changes += 1
      new_row.append(new_state)
    new_layout.append(''.join(new_row))
  return new_layout, state_changes

def get_new_state(layout, row, col, sighted_seats_by_seat):
  current = layout[row][col]
  if current == 'L':
    return '#' if not seats_sighted_from(layout, col, row, sighted_seats_by_seat).count('#') else 'L'
  elif current == '#':
    return 'L' if seats_sighted_from(layout, col, row, sighted_seats_by_seat).count('#') >= 5 else '#'
  else:
    return '.'

def calc_occupied_seats(layout):
  return sum(row.count('#') for row in layout)

def seats_sighted_from(layout, x, y, sighted_seats_by_seat):
  return [state_of(layout, seat) for seat in sighted_seats_by_seat[x][y]]

def state_of(layout, seat):
  return layout[seat[1]][seat[0]]

def occupied_adjacent(layout, row, col, sighted_seats_by_seat):
  for adjacent in sighted_seats_by_seat[col][row]:
    if is_occupied(layout, adjacent):
      return True
  return False

def five_or_more_neighbours(layout, row, col, sighted_seats_by_seat):
  count_occupied = 0
  for adjacent in sighted_seats_by_seat[col][row]:
    if is_occupied(layout, adjacent):
      count_occupied += 1
  return count_occupied >= 5

def is_occupied(layout, seat):
  return layout[seat[1]][seat[0]] == '#'

def adjacents(layout, row, col):
  width = len(layout[0])
  height = len(layout)
  found = None
  # up
  for y in range(row-1, -1, -1):
    seat = layout[y][col]
    if seat in ['#', 'L']:
      found = [col, y]
      break
  if found:
    yield found
  found = None
  # down
  for y in range(row+1, height):
    seat = layout[y][col]
    if seat in ['#', 'L']:
      found = [col, y]
      break
  if found:
    yield found
  found = None
  # left
  for x in range(col-1, -1, -1):
    seat = layout[row][x]
    if seat in ['#', 'L']:
      found = [x, row]
      break
  if found:
    yield found
  found = None
  # right
  for x in range(col+1, width):
    seat = layout[row][x]
    if seat in ['#', 'L']:
      found = [x, row]
      break
  if found:
    yield found
  found = None
  # up-left
  steps = min(row, col)
  for i in range(1, steps+1):
    if row-i >= 0 and col-i >= 0:
      seat = layout[row-i][col-i]
      if seat in ['#', 'L']:
        found = [col-i, row-i]
        break
  if found:
    yield found
  found = None
  # up-right
  steps = min(row, width-col-1) # maybe wrong?
  for i in range(1, steps+1):
    if row-i >= 0 and col+i < width:
      seat = layout[row-i][col+i]
      if seat in ['#', 'L']:
        found = [col+i, row-i]
        break
  if found:
    yield found
  found = None
  # down-left
  steps = min(height-row-1, col) # maybe wrong?
  for i in range(1, steps+1):
    if row+i < height and col-i >= 0:
      seat = layout[row+i][col-i]
      if seat in ['#', 'L']:
        found = [col-i,row+i]
        break
  if found:
    yield found
  found = None
  # down-right
  steps = min(height-row-1, width-col-1) # maybe wrong?
  for i in range(1, steps+1):
    if row+i < height and col+i < width:
      seat = layout[row+i][col+i]
      if seat in ['#', 'L']:
        found = [col+i,row+i]
        break
  if found:
    yield found

if __name__ == '__main__':
  print(run(sys.stdin.read()))
