import sys
from math import prod

def run(input):
  candidate_pairs_by_remainder = dict()
  checked_entries = set()
  for entry in entries(input):
    if entry in candidate_pairs_by_remainder:
      return entry * prod(candidate_pairs_by_remainder[entry])
    else:
      for checked_entry in checked_entries:
        remainder = 2020 - checked_entry - entry
        if remainder > 0:
          candidate_pairs_by_remainder[remainder] = (entry, checked_entry)
      checked_entries.add(entry)

def entries(input):
  lines = input.splitlines()
  line_count = len(lines)
  i = 0
  while i < line_count:
    yield int(lines[i])
    i += 1

if __name__ == '__main__':
  print(run(sys.stdin.read()))
