import sys
from math import prod

def run(input):
  grid = input.splitlines()
  slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
  return prod([check_slope(grid, slope) for slope in slopes])

def check_slope(grid, slope):
  row = 0
  col = 0
  hit_trees = 0
  while row+1 < len(grid):
    row += slope[0]
    col += slope[1]
    if grid[row][col % len(grid[row])] == '#':
      hit_trees += 1
  return hit_trees

if __name__ == '__main__':
  print(run(sys.stdin.read()))
