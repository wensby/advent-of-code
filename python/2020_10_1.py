import sys

def run(input):
  adapters = sorted(int(line) for line in input.splitlines())
  current_jolt = 0
  diffs = { 1: 0, 2: 0, 3: 0 }
  for adapter in adapters:
    diffs[adapter - current_jolt] += 1
    current_jolt = adapter
  diffs[3] += 1
  return diffs[1] * diffs[3]

if __name__ == '__main__':
  print(run(sys.stdin.read()))
