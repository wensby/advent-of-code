import sys

def run(input):
  rules = parse_rules(input)
  final_contents = get_contents(rules, 1, 'shiny gold')
  return sum(count for count in final_contents.values())

def parse_rules(input):
  return {parse_bagtype(line): parse_content(line) for line in input.splitlines()}

def parse_bagtype(line):
  return ' '.join(line.split(' ')[:2])

def parse_content(line):
  if 'no other bags' in line:
    return dict()
  content_part = line.split(' contain ')[1][:-1].replace(' bags', '').replace(' bag', '')
  count_by_bag_colors = {' '.join(x.split(' ')[1:]): int(x.split(' ')[0]) for x in content_part.split(', ')}
  return count_by_bag_colors

def resolve_final_contents(rules):
  return {bag: get_contents(rules, 1, bag) for bag in rules}
    
def get_contents(rules, count, bag):
  direct_contents = rules[bag]
  count_adjusted = {b: c * count for b, c in direct_contents.items()}
  result = {k: v for k, v in count_adjusted.items()}
  for contained_bag, count in count_adjusted.items():
    contained_bags_content = get_contents(rules, count, contained_bag)
    for k, v in contained_bags_content.items():
      result[k] = result.get(k, 0) + v
  return result

if __name__ == '__main__':
  print(run(sys.stdin.read()))
