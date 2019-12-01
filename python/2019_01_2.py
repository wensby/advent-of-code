import sys

def fuel_requirement(mass):
  fuel_mass = max(0, mass // 3 - 2)
  return fuel_mass + fuel_requirement(fuel_mass) if fuel_mass > 0 else fuel_mass

def parse_module_masses(input):
  return map(int, input.splitlines())

def run(input):
  return sum(map(fuel_requirement, parse_module_masses(input)))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
