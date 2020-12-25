import sys
from math import prod

def solve(input):
  solved_ticket = solve_your_ticket(input)
  return prod([v for k, v in solved_ticket.items() if k.startswith('departure')])

def solve_your_ticket(input):
  field_rules = parse_field_rules(input)
  nearby_tickets = parse_nearby_tickets(input)
  your_ticket = parse_your_ticket(input)
  valid_nearby_tickets = [t for t in nearby_tickets if is_valid_ticket(t, field_rules)]
  all_valid_tickets = valid_nearby_tickets + [your_ticket]
  field_order = solve_field_order(all_valid_tickets, field_rules)
  return {field_order[i]: your_ticket[i] for i in range(len(field_order))}

def solve_field_order(tickets, rules):
  all_field_names = {r['name'] for r in rules}
  matching_rules_by_index = {i: set(all_field_names) for i in range(len(tickets[0]))}
  for i in range(len(tickets[0])):
    for field in list(matching_rules_by_index[i]):
      rule = [r for r in rules if r['name'] == field][0]
      if not is_rule_valid_for_field_by_index(rule, tickets, i):
        matching_rules_by_index[i].remove(field)
  result = solve_field_orders(tickets, 0, rules, matching_rules_by_index)
  return [x['name'] for x in result]

def solve_field_orders(tickets, index, remaining_rules, matching_rules_by_index):
  if not remaining_rules:
    return []
  matching_rules = [r for r in remaining_rules if r['name'] in matching_rules_by_index[index]]
  if not matching_rules:
    return False
  for matching_rule in matching_rules:
    recursive_result = solve_field_orders(tickets, index+1, [r for r in remaining_rules if r['name'] != matching_rule['name']], matching_rules_by_index)
    if recursive_result is not False:
      return [matching_rule] + recursive_result
  return False

def parse_your_ticket(input):
  return [int(x) for x in input.split('\n\n')[1].splitlines()[1].split(',')]

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

def is_valid_ticket(ticket, field_rules):
  for value in ticket:
    if not is_valid(value, field_rules):
      return False
  return True

def is_valid(value, field_rules):
  for ranges in field_rules:
    for range in ranges['ranges']:
      if range[0] <= value <= range[1]:
        return True
  return False

def is_rule_valid_for_field_by_index(rule, tickets, index):
  for ticket in tickets:
    any_range_match = False
    for range in rule['ranges']:
      if range[0] <= ticket[index] <= range[1]:
        any_range_match = True
    if not any_range_match:
      return False
  return True

if __name__ == '__main__':
  print(solve(sys.stdin.read()))
