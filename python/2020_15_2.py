import sys

def solve(input):
  # setup starting conditions
  numbers = [int(x) for x in input.rstrip('\n').split(',')]
  finished_turns = 0
  previous_number = None
  previous_number_previous_turn = None
  turn_by_number = {}
  previous_overwritten = None

  # go through starting numbers
  for i in range(len(numbers)):
    turn = i + 1
    number = numbers[i]
    previous_number_previous_turn = turn_by_number.get(number, None)
    turn_by_number[number] = turn
    previous_number = number
    finished_turns = turn
  
  while finished_turns < 30000000:
    turn = finished_turns + 1
    if previous_number_previous_turn:
      next_number = turn_by_number[previous_number] - previous_number_previous_turn
    else:
      next_number = 0
    previous_number_previous_turn = turn_by_number.get(next_number, None)
    turn_by_number[next_number] = turn
    previous_number = next_number
    finished_turns = turn

  return previous_number


if __name__ == '__main__':
  print(solve(sys.stdin.read()))
