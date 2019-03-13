import sys
from collections import namedtuple

Rectangle = namedtuple('Rectangle', 'area')
Present = namedtuple('Present', 'surfaces')

def create_present(length, width, height):
  surfaces = [
    Rectangle(length * width),
    Rectangle(width * height),
    Rectangle(height * length)
  ]
  return Present(surfaces + surfaces)

def calc_required_paper(present):
  areas = list(map(lambda s : s.area, present.surfaces))
  return sum(areas) + min(areas)

def parse_dimensions(line):
  return list(map(int, line.split('x')))

def parse_present(line):
  dimensions = parse_dimensions(line)
  return create_present(dimensions[0], dimensions[1], dimensions[2])

def parse_presents(input):
  return map(parse_present, input.splitlines())

def run(input):
  return sum(map(calc_required_paper, parse_presents(input)))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
