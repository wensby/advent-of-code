import sys

def run(input):
  checked_entries = set()
  for entry in entries(input):
    if 2020-entry in checked_entries:
      return entry * (2020-entry)
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
