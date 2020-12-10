import sys
import math

def run(input):
  adapters = sorted(int(line) for line in input.splitlines())
  return calc_configurations(adapters)

def calc_configurations(adapters):
  adapters.insert(0, 0)
  adapters.append(adapters[-1]+3)
  diffs = get_diffs(adapters)
  parts = split_by_3_diff(diffs)
  for part in parts:
    print(part)
  return math.prod(calc_part_configurations(part) for part in parts)

def calc_part_configurations(part):
  if len(part) == 1:
    return 1
  elif len(part) == 2:
    return 2
  elif len(part) == 3:
    return 4
  elif len(part) == 4:
    return 7


def get_diffs(adapters):
  return [adapters[i]-adapters[i-1] for i in range(1, len(adapters))]

def split_by_3_diff(diffs):
  parts = []
  part = []
  for diff in diffs:
    if diff == 3:
      if part:
        parts.append(part)
        part = []
    else:
      part.append(diff)
  return parts

if __name__ == '__main__':
  print(run(sys.stdin.read()))
