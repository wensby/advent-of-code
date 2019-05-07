import sys, re
from collections import namedtuple
from functools import reduce

Claim = namedtuple('Claim', ['id', 'topleft', 'dimensions'])

claim_pattern = re.compile('^#([0-9]+) @ ([0-9,]+): ([0-9x]+)$')
coordinates_pattern = re.compile('^([0-9]+),([0-9]+)$')
dimension_pattern = re.compile('^([0-9]+)x([0-9]+)$')

def run(input):
  claims = parse_claims(input)
  return calc_overlapping_squares(claims)

def calc_overlapping_squares(claims):
  fabric = [[0 for x in range(1000)] for x in range(1000)]
  overlaps = 0
  for claim in claims:
    overlaps = overlaps + place_claim_and_get_new_overlaps(claim, fabric)
  return overlaps

def place_claim_and_get_new_overlaps(claim, fabric):
  new_overlaps = 0
  for y in range(claim.topleft[1], claim.topleft[1] + claim.dimensions[1]):
    for x in range(claim.topleft[0], claim.topleft[0] + claim.dimensions[0]):
      previous = fabric[y][x]
      if previous < 2:
        fabric[y][x] = previous + 1
      if previous == 1:
        new_overlaps = new_overlaps + 1
  return new_overlaps

def parse_claims(input):
  return map(parse_claim, input.splitlines())

def parse_claim(line):
  match = claim_pattern.match(line)
  id = int(match.group(1))
  topleft = parse_coordinates(match.group(2))
  dimensions = parse_dimension(match.group(3))
  return Claim(id, topleft, dimensions)

def parse_coordinates(coordinates):
  match = coordinates_pattern.match(coordinates)
  return (int(match.group(1)), int(match.group(2)))

def parse_dimension(dimension):
  match = dimension_pattern.match(dimension)
  return (int(match.group(1)), int(match.group(2)))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
