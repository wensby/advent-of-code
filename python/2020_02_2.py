import sys

def run(input):
  return len([line for line in input.splitlines() if is_valid(line)])

def is_valid(line):
  policy, password = line.split(': ')
  first, second = (int(position)-1 for position in policy.split(' ')[0].split('-'))
  letter = policy[-1]
  return (password[first] == letter) ^ (password[second] == letter)

if __name__ == '__main__':
  print(run(sys.stdin.read()))
