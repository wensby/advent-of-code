import sys
import pprint

def solve(input):
  numbers = [int(x) for x in input.rstrip('\n').split(',')]
  finished_turns = len(numbers)
  previous_number = numbers[-1]
  number_positions = {}
  for pos in range(len(numbers)):
    number = numbers[pos]
    number_positions[number] = number_positions.get(number, []) + [pos + 1]
  while finished_turns < 2020:
    turn = finished_turns + 1
    next_number = figure_out_next_number(number_positions, previous_number)
    number_positions[next_number] = number_positions.get(next_number, []) + [turn]
    previous_number = next_number
    finished_turns += 1
  return previous_number

def figure_out_next_number(number_positions, previous_number):
  occurrences = number_positions[previous_number]
  if len(occurrences) == 1:
    return 0
  else:
    return occurrences[-1] - occurrences[-2]

if __name__ == '__main__':
  print(solve(sys.stdin.read()))
