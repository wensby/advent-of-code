import sys
from collections import namedtuple
from functools import reduce

Present = namedtuple('Present', 'dimensions')

def calc_wrap_ribbon(present):
  present.dimensions.sort()
  return 2 * (present.dimensions[0] + present.dimensions[1])

def calc_bow_ribbon(present):
  return reduce(lambda x, y: x * y, present.dimensions)

def calc_ribbon(present):
  return calc_wrap_ribbon(present) + calc_bow_ribbon(present)

def parse_present(line):
  return Present(list(map(int, line.split('x'))))

def parse_presents(input):
  return map(parse_present, input.splitlines())

def run(input):
  return sum(map(calc_ribbon, parse_presents(input)))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
