import sys
import re
import itertools

class Moon:

  def __init__(self, position, velocity):
    self._position = position
    self._velocity = velocity

  def get_position(self):
    return self._position

  def pull_towards(self, position):
    self._velocity = tuple(map(lambda x: self._new_axis(x, position), range(3)))

  def _new_axis(self, i, position):
    if self._position[i] < position[i]:
      return self._velocity[i] + 1
    elif self._position[i] > position[i]:
      return self._velocity[i] - 1
    return self._velocity[i]

  def __repr__(self):
    return f'pos={self._position}, vel={self._velocity}'

  def apply_velocity(self):
    self._position = tuple(map(sum, zip(self._position, self._velocity)))

  def total_energy(self):
    return self.potential_energy() * self.kinetic_energy()

  def potential_energy(self):
    return sum(map(abs, self._position))

  def kinetic_energy(self):
    return sum(map(abs, self._velocity))

class Simulation:

  def __init__(self, moons):
    self._moons = moons

  def run(self, steps):
    for i in range(steps):
      self._step()

  def _step(self):
    self._apply_gravity()
    self._apply_velocity()

  def _apply_gravity(self):
    for pair in itertools.combinations(self._moons, 2):
      a_pos = pair[0].get_position()
      b_pos = pair[1].get_position()
      pair[0].pull_towards(b_pos)
      pair[1].pull_towards(a_pos)

  def _apply_velocity(self):
    for moon in self._moons:
      moon.apply_velocity()

def run(input):
  moons = parse_moons(input)
  simulation = create_simulation(moons)
  simulation.run(1000)
  return calc_total_energy(moons)

def parse_moons(input):
  return list(map(parse_moon, input.splitlines()))

def parse_moon(line):
  position = parse_vector3(line)
  return Moon(position, (0, 0, 0))

def parse_vector3(string):
  pattern = re.compile(r'<x=(.*), ?y=(.*), ?z=(.*)>')
  match = pattern.match(string)
  return (int(match.group(1)), int(match.group(2)), int(match.group(3)))

def create_simulation(moons):
  return Simulation(moons)

def calc_total_energy(moons):
  return sum(map(lambda x: x.total_energy(), moons))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
