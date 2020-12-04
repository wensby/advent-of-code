import sys
import re

def is_valid_hgt(x):
  valid_metric = x.endswith('cm') and 150 <= float(x[:-2]) <= 193
  valid_imperial = x.endswith('in') and 59 <= float(x[:-2]) <= 76
  return valid_metric or valid_imperial

required_fields = {
    'byr': lambda x: x.isnumeric() and 1920 <= int(x) <= 2002,
    'iyr': lambda x: x.isnumeric() and 2010 <= int(x) <= 2020,
    'eyr': lambda x: x.isnumeric() and 2020 <= int(x) <= 2030,
    'hgt': is_valid_hgt,
    'hcl': lambda x: re.match(r'#[0-9a-f]{6}', x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: x.isnumeric() and len(x) == 9,
    'cid': lambda x: True
}

def run(input):
  passports = parse_passports(input)
  return len([p for p in passports if is_valid(p)])

def parse_passports(input):
  passports = []
  passport = {}
  passports.append(passport)
  for line in input.splitlines():
    if not line:
      passport = {}
      passports.append(passport)
    else:
      for field in line.split(' '):
        key, value = field.split(':')
        passport[key] = value
  return passports

def is_valid(passport):
  missing_fields = [f for f in required_fields if f not in passport.keys()]
  for key, value in passport.items():
    if key in required_fields and not required_fields[key](value):
      return False
  return not missing_fields or missing_fields == ['cid']

if __name__ == '__main__':
  print(run(sys.stdin.read()))
