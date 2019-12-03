import sys
import math

def run(input):
  wire_paths = parse_wire_paths(input)
  intersections = find_intersection_coords(wire_paths)
  return min(map(lambda coord: steps_to_coord(wire_paths, coord), intersections))

def parse_wire_paths(input):
  return list(map(parse_wire_path, input.splitlines()))

def find_intersection_coords(wire_paths):
  first_wire_coords = {coord for coord in wire_paths[0]}
  return [coord for coord in wire_paths[1] if coord in first_wire_coords]

def steps_to_coord(wire_paths, coord):
  return wire_paths[0].index(coord)+1 + wire_paths[1].index(coord)+1

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
