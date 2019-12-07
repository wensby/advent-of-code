import sys

class OrbitTransferCalculator:

  def __init__(self, orbit_map):
    self._orbit_map = orbit_map

  def calculate_transfers_between(self, origin, destination):
    origin_path = self._get_full_orbital_path(origin)
    destination_path = self._get_full_orbital_path(destination)
    common_path = list(set(origin_path).intersection(destination_path))
    return len(origin_path) + len(destination_path) - 2*len(common_path) 

  def _get_full_orbital_path(self, object):
    path = [object]
    while path[-1] != 'COM':
      path.append(self._orbit_map[path[-1]])
    return path[::-1]


def run(input):
  orbit_map = parse_orbit_map(input)
  current = orbit_map['YOU']
  destination = orbit_map['SAN']
  calculator = OrbitTransferCalculator(orbit_map)
  return calculator.calculate_transfers_between(current, destination)

def parse_orbit_map(input):
  orbits = list(map(lambda x: x.split(')'), input.splitlines()))
  return { b: a for a, b in orbits }

if __name__ == '__main__':
  print(run(sys.stdin.read()))
