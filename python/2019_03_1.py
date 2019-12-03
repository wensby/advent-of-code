import sys
import math

def run(input):
  wire_paths = parse_wire_paths(input)
  return find_closest_intersection(wire_paths)

def parse_wire_paths(input):
  return list(map(parse_wire_path, input.splitlines()))

def parse_wire_path(line):
  coords = []
  pos = (0, 0)
  for part in line.split(','):
    direction = part[0]
    steps = int(part[1:])
    next_coords = get_next_coords(pos, direction, steps)
    pos = next_coords[-1]
    coords.extend(next_coords)
  return coords

def find_closest_intersection(wire_paths):
  first_wire_visited = { coord for coord in wire_paths[0] }
  closest_distance = math.inf
  for coord in wire_paths[1]:
    if coord in first_wire_visited:
      distance = abs(coord[0]) + abs(coord[1])
      if distance < closest_distance:
        closest_distance = distance
  return closest_distance

def get_next_coords(org, direction, steps):
  x, y = org
  if direction in 'U':
    new_coord = lambda step : (x, y+step)
  elif direction == 'D':
    new_coord = lambda step : (x, y-step)
  elif direction == 'R':
    new_coord = lambda step : (x+step, y)
  else:
    new_coord = lambda step : (x-step, y)
  return [ new_coord(step) for step in range(1, steps+1) ]

if __name__ == '__main__':
  print(run(sys.stdin.read()))
