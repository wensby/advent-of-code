import math
import sys

class AsteroidField:

  def __init__(self, width, height, asteroids):
    self.width = width
    self.height = height
    self.asteroids_by_position = { a.position: a for a in asteroids }

class Asteroid:

  def __init__(self, position):
    self.position = position

def run(input):
  field = parse_field(input)
  asteroid = find_monitoring_station_asteroid(field)
  vaporized = get_vaporization_order(asteroid, field)
  two_hundredth = vaporized[199]
  return two_hundredth[0] * 100 + two_hundredth[1]

def parse_field(input):
  asteroids = []
  rows = input.splitlines()
  for y in range(len(rows)):
    row = rows[y]
    for x in range(len(row)):
      if row[x] == '#':
        asteroids.append(Asteroid((x,y)))
  return AsteroidField(len(rows), len(rows[0]), asteroids)

def find_monitoring_station_asteroid(field):
  best_candidate_visible_asteroids = 0
  best_candidate = None
  for asteroid in field.asteroids_by_position.values():
    visible_asteroids = len(get_visible_asteroids(asteroid, field))
    if visible_asteroids > best_candidate_visible_asteroids:
      best_candidate_visible_asteroids = visible_asteroids
      best_candidate = asteroid
  return best_candidate

def get_vaporization_order(asteroid, field):
  order = []
  remaining_asteroids = field.asteroids_by_position.copy()
  del remaining_asteroids[asteroid.position]
  while len(remaining_asteroids) > 0:
    field = AsteroidField(field.width, field.height, remaining_asteroids.values())
    surrounding_asteroids = get_visible_asteroids(asteroid, field)
    surrounding_asteroids.sort(key=lambda x: angle(asteroid.position, x))
    for target_pos in surrounding_asteroids:
      order.append(target_pos)
      del remaining_asteroids[target_pos]
  return order

def angle(start, end):
  dy = start[1] - end[1]
  dx = end[0] - start[0]
  theta = math.atan2(dy, dx)
  angle = theta * 180/math.pi
  return convert_angle(angle)

def convert_angle(angle):
  positive_angle = (angle + 360 % 360)
  return (360 - positive_angle + 90) % 360

def get_visible_asteroids(asteroid, field):
  candidate_visibles = set(field.asteroids_by_position.keys())
  if asteroid.position in candidate_visibles:
    candidate_visibles.remove(asteroid.position)
  hidden = set()
  for pos in candidate_visibles:
    if pos not in hidden:
      delta = get_delta(asteroid.position, pos)
      hidden.update(get_hidden_positions_behind(pos, delta, field))
  return [pos for pos in candidate_visibles if pos not in hidden]

def get_delta(a, b):
  delta = (b[0] - a[0], b[1] - a[1])
  gcd = math.gcd(delta[0], delta[1])
  return (delta[0]//gcd, delta[1]//gcd)

def get_hidden_positions_behind(origin, delta, field):
  hidden = set()
  next_behind = (origin[0]+delta[0], origin[1]+delta[1])
  while next_behind[0] >= 0 and next_behind[1] >= 0 and next_behind[0] < field.width and next_behind[1] < field.height:
    hidden.add(next_behind)
    next_behind = (next_behind[0]+delta[0], next_behind[1]+delta[1])
  return hidden

if __name__ == '__main__':
  print(run(sys.stdin.read()))
