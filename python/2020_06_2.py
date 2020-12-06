import sys

def run(input):
  groups = parse_groups(input)
  sum = 0
  for group in groups:
    sum += len(group[0].intersection(*group))
  return sum

def parse_groups(input):
  groups = []
  group = []
  groups.append(group)
  for line in input.splitlines():
    if not line:
      group = []
      groups.append(group)
    else:
      group.append(set(line))
  return groups

if __name__ == '__main__':
  print(run(sys.stdin.read()))
