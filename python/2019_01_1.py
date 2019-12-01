import sys

def module_fuel_requirement(mass):
  return max(0, mass // 3 - 2)

def parse_module_masses(input):
  return map(int, input.splitlines())

def run(input):
  return sum(map(module_fuel_requirement, parse_module_masses(input)))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
