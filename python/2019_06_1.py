import sys

class OrbitTransferCalculator:

  def __init__(self, orbit_map, origin):
    self._orbit_map = orbit_map
    self._origin = origin

  def calculate_transfers_to(self, destination):
    origin_path = self._get_path_from_com(self._origin)
    destination_path = self._get_path_from_com(destination)
    return abs(len(origin_path) - len(destination_path))

  def _get_path_from_com(self, object):
    path = [object]
    while path[-1] != 'COM':
      path.append(self._orbit_map[path[-1]])
    return path[::-1]


def run(input):
  orbit_map = parse_orbit_map(input)
  calculator = OrbitTransferCalculator(orbit_map, 'COM')
  total = 0
  for object in orbit_map:
    total += calculator.calculate_transfers_to(object)
  return total

def parse_orbit_map(input):
  orbits = list(map(lambda x: x.split(')'), input.splitlines()))
  return { b: a for a, b in orbits }

if __name__ == '__main__':
  print(run(sys.stdin.read()))
