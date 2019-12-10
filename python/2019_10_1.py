from copy import deepcopy
import sys
from math import gcd

def run(input):
  field = parse_field(input)
  best_candidate = None
  best_candidate_visible_asteroids = 0
  for row in range(len(field)):
    for col in range(len(field[row])):
      if field[row][col]: # is asteroid
        visible_asteroids = calc_visible_asteroids_from((col, row), field)
        if visible_asteroids > best_candidate_visible_asteroids:
          best_candidate_visible_asteroids = visible_asteroids
          best_candidate = (col, row)
  return best_candidate_visible_asteroids

def parse_field(input):
  return [ [ char == '#' for char in row ] for row in input.splitlines() ]

def calc_visible_asteroids_from(pos, field):
  visible_asteroids = deepcopy(field)
  for row in range(len(visible_asteroids)):
    for col in range(len(visible_asteroids[row])):
      if visible_asteroids[row][col]:
        if (col, row) == pos:
          visible_asteroids[row][col] = False
        else:
          delta = (col-pos[0], row-pos[1])
          normalized_delta = normalize(delta)
          darken_from((col, row), visible_asteroids, normalized_delta)
  return sum(map(lambda x: x.count(True), visible_asteroids))

def darken_from(pos, field, delta):
  pos = (pos[0]+delta[0], pos[1]+delta[1])
  while is_inside(pos, field):
    field[pos[1]][pos[0]] = False
    pos = (pos[0]+delta[0], pos[1]+delta[1])

def is_inside(pos, field):
  col = pos[0]
  row = pos[1]
  return row >= 0 and row < len(field) and col >= 0 and col < len(field[row])

def normalize(delta):
  if delta[0] and not delta[1]:
    return (delta[0]//abs(delta[0]), delta[1])
  elif delta[1] and not delta[0]:
    return (delta[0], delta[1]//abs(delta[1]))
  else:
    divisor = gcd(delta[0], delta[1])
    return (delta[0]//abs(divisor), delta[1]//abs(divisor))


if __name__ == '__main__':
  print(run(sys.stdin.read()))
