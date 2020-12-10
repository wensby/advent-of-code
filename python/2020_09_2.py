import sys

def run(input):
  return solve_with_custom_pool_size(input, 25)

def solve_with_custom_pool_size(input, pool_size):
  numbers = [int(line) for line in input.splitlines()]
  trouble_number = find_trouble_number(numbers, pool_size)
  return find_encryption_weakness(numbers, trouble_number)

def find_trouble_number(numbers, pool_size):
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

def find_encryption_weakness(numbers, trouble_number):
  for first in range(0, len(numbers)):
    sum = 0
    for i in range(first, len(numbers)):
      sum += numbers[i]
      if sum > trouble_number:
        break
      if sum == trouble_number:
        return sum_of_smallest_and_largest(numbers[first:i+1])

def sum_of_smallest_and_largest(numbers):
  return min(numbers) + max(numbers)

if __name__ == '__main__':
  print(run(sys.stdin.read()))
