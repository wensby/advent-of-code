import sys
import pprint

def solve(input):
  state = {}
  x = 0
  for x_line in input.splitlines():
    current_x = {}
    y = 0
    for cube in x_line:
      current_x[y] = { 0: {0: cube } }
      y += 1
    state[x] = current_x
    x += 1

  done_cycles_count = 0
  while done_cycles_count < 6:
    state = run_cycle(state)
    done_cycles_count += 1

  active_sum = 0
  for xyzw in state.values():
    for yzw in xyzw.values():
      for zw in yzw.values():
        for w in zw.values():
          if w == '#':
            active_sum += 1
  return active_sum

def run_cycle(state):
  new_state = {}
  coordinates_of_interest = {}
  for x, xyzw in state.items():
    for y, yzw in xyzw.items():
      for z, zw in yzw.items():
        for w, cube in zw.items():
          if cube == '#':
            add_surrounding_coordinates(coordinates_of_interest, (x,y,z,w))
  for x in coordinates_of_interest:
    for y in coordinates_of_interest[x]:
      for z in coordinates_of_interest[x][y]:
        for w in coordinates_of_interest[x][y][z]:
          new_state.setdefault(x, {}).setdefault(y, {}).setdefault(z, {})[w] = find_next_state(state, (x, y, z, w))
  return new_state
          
empty = {}

def get_coordinate_state(state, coordinates):
  x, y, z, w = coordinates
  return state.get(x, empty).get(y, empty).get(z, empty).get(w, '.')


def find_next_state(old_state, coordinates):
  currently_active = get_coordinate_state(old_state, coordinates) == '#'
  active_neighbours = 0
  for n in iterate_neighbour_activity(old_state, coordinates):
    active_neighbours += 1 if n else 0
    if active_neighbours > 3:
      if currently_active:
        return '.'
      else:
        return '.'
  if currently_active:
    return '.' if active_neighbours < 2 else '#'
  else:
    return '.' if active_neighbours < 3 else '#'

def iterate_neighbour_activity(old_state, coordinates):
  x_mid, y_mid, z_mid, w_mid = coordinates
  for x in range(x_mid-1, x_mid+2):
    for y in range(y_mid-1, y_mid+2):
      for z in range(z_mid-1, z_mid+2):
        for w in range(w_mid-1, w_mid+2):
          if not (x == x_mid and y == y_mid and z == z_mid and w == w_mid):
            yield get_coordinate_state(old_state, (x, y, z, w)) == '#'

def add_surrounding_coordinates(collection, middle):
  x_mid, y_mid, z_mid, w_mid = middle
  for x in range(x_mid-1, x_mid+2):
    for y in range(y_mid-1, y_mid+2):
      for z in range(z_mid-1, z_mid+2):
        for w in range(w_mid-1, w_mid+2):
          collection.setdefault(x, {}).setdefault(y, {}).setdefault(z, set()).add(w)

if __name__ == '__main__':
  print(solve(sys.stdin.read()))
