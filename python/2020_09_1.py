import sys

def run(input):
  return solve_with_custom_pool_size(input, 25)

def solve_with_custom_pool_size(input, pool_size):
  numbers = [int(line) for line in input.splitlines()]
  pool = numbers[:pool_size]
  index = pool_size
  while is_pool_sum(numbers[index], pool):
    pool.pop(0)
    pool.append(numbers[index])
    index += 1
  return numbers[index]

def is_pool_sum(number, pool):
  sought = set()
  for pool_number in pool:
    if pool_number in sought:
      return True
    diff = number - pool_number
    if diff >= 0:
      sought.add(diff)
  return False

if __name__ == '__main__':
  print(run(sys.stdin.read()))
