import sys

rows = 128
cols = 8

def run(input):
  ids = [parse_seat(x)[2] for x in input.splitlines()]
  last = None
  for id in sorted(ids):
    if last and id > last+1:
      return id-1
    else:
      last = id

def parse_seat(subject):
  row = find_row(subject[:7])
  col = find_col(subject[7:])
  return (row, col, row*8 + col)

def find_row(subject):
  return binary_space_partition(0, rows, subject, 'F')

def find_col(subject):
  return binary_space_partition(0, cols, subject, 'L')

def binary_space_partition(low, high, subject, low_char):
  if not subject:
    return int(low)
  elif subject[0] == low_char:
    return binary_space_partition(low, high - (high-low)/2, subject[1:], low_char)
  else:
    return binary_space_partition(low + (high-low)/2, high, subject[1:], low_char)

if __name__ == '__main__':
  print(run(sys.stdin.read()))
