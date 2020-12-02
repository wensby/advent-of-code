import sys

def run(input):
  return len([line for line in input.splitlines() if is_valid(line)])

def is_valid(line):
  policy, password = line.split(': ')
  min, max = (int(n) for n in policy.split(' ')[0].split('-'))
  letter = policy[-1]
  return min <= password.count(letter) <= max

if __name__ == '__main__':
  print(run(sys.stdin.read()))
