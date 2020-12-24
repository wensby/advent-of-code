import sys
import pprint

def solve(input):
  field_rules = parse_field_rules(input)
  nearby_tickets = parse_nearby_tickets(input)
  invalid_field_values = find_invalid_field_values(nearby_tickets, field_rules)
  return sum(invalid_field_values)

def parse_field_rules(input):
  result = []
  for line in input.split('\n\n')[0].splitlines():
    splitline = line.split(': ')
    name = splitline[0]
    ranges = {tuple([int(n) for n in r.split('-')]) for r in splitline[1].split(' or ')}
    result.append({'name': name, 'ranges': ranges})
  return result

def parse_nearby_tickets(input):
  result = []
  for line in input.split('\n\n')[2].splitlines()[1:]:
    result.append([int(v) for v in line.split(',')])
  return result

def find_invalid_field_values(nearby_tickets, field_rules):
  result = []
  for ticket in nearby_tickets:
    for value in ticket:
      if not is_valid(value, field_rules):
        result.append(value)
  return result

def is_valid(value, field_rules):
  for ranges in field_rules:
    for range in ranges['ranges']:
      if range[0] <= value <= range[1]:
        return True
  return False

if __name__ == '__main__':
  print(solve(sys.stdin.read()))
