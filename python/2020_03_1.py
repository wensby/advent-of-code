import sys

def run(input):
  slope = input.splitlines()
  row = 0
  col = 0
  hit_trees = 0
  while row+1 < len(slope):
    row += 1
    col += 3
    if slope[row][col % len(slope[row])] == '#':
      hit_trees += 1
  return hit_trees

if __name__ == '__main__':
  print(run(sys.stdin.read()))
