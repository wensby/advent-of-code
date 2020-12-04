import sys

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

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
  return not missing_fields or missing_fields == ['cid']
    

if __name__ == '__main__':
  print(run(sys.stdin.read()))
