import sys
import re
import itertools
import math

class AxisSimulation:

  def __init__(self, positions, velocities):
    self._positions = positions
    self._velocities = velocities

  def step(self):
    self._apply_gravity()
    self._apply_velocity()

  def state(self):
    return tuple(self._positions + self._velocities)

  def _apply_gravity(self):
    for pair in itertools.combinations(range(4), 2):
      a_pos = self._positions[pair[0]]
      b_pos = self._positions[pair[1]]
      a_vel = self._velocities[pair[0]]
      b_vel = self._velocities[pair[1]]
      if a_pos < b_pos:
        self._velocities[pair[0]] = a_vel + 1
        self._velocities[pair[1]] = b_vel - 1
      if a_pos > b_pos:
        self._velocities[pair[0]] = a_vel - 1
        self._velocities[pair[1]] = b_vel + 1

  def _apply_velocity(self):
    for i in range(4):
      self._positions[i] += self._velocities[i]

def run(input):
  positions = parse_positions(input)
  velocities = [[0, 0, 0]]*4
  x_cycle = find_axis_cycle(positions, velocities, 0)
  y_cycle = find_axis_cycle(positions, velocities, 1)
  z_cycle = find_axis_cycle(positions, velocities, 2)
  return lcm(x_cycle, y_cycle, z_cycle)

def lcm(a, b, c):
  res = a
  for i in [b, c]:
    res = res*i//math.gcd(res, i)
  return res

def find_axis_cycle(positions, velocities, i):
  simulation = create_axis_simulation(positions, velocities, i)
  states = {simulation.state()}
  steps = 0
  while True:
    simulation.step()
    steps += 1
    state = simulation.state()
    if state in states:
      return steps
    states.add(state)

def get_state(moons):
  return tuple(map(lambda x: x.get_state(), moons))

def parse_positions(input):
  return list(map(parse_position, input.splitlines()))

def parse_position(line):
  return parse_vector3(line)

def parse_vector3(string):
  pattern = re.compile(r'<x=(.*), ?y=(.*), ?z=(.*)>')
  match = pattern.match(string)
  return [int(match.group(1)), int(match.group(2)), int(match.group(3))]

def create_axis_simulation(positions, velocities, i):
  i_positions = [x[i] for x in positions]
  i_velocities = [x[i] for x in velocities]
  return AxisSimulation(i_positions, i_velocities)

if __name__ == '__main__':
  print(run(sys.stdin.read()))
