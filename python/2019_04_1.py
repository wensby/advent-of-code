import sys
import re

same_adjacent = re.compile(r'([0-9])\1')

def run(input):
  count = 0
  password_range = list(map(int, input.split('-')))
  password = password_range[0]
  while password <= password_range[1]:
    descending_digit_index = find_descending_digit_index(password)
    if descending_digit_index:
      password = get_next_non_descending(password, descending_digit_index-1)
    else:
      if same_adjacent.search(str(password)):
        count += 1
      password += 1
  return count

def find_descending_digit_index(number):
  strnum = str(number)
  for i in range(1, len(strnum)):
    if int(strnum[i-1]) > int(strnum[i]):
      return i
  return None

def get_next_non_descending(number, from_index):
  numberstr = str(number)
  beginning = numberstr[0:from_index]
  last_ok_digit = numberstr[from_index]
  return int(beginning + last_ok_digit*(len(numberstr) - from_index))

if __name__ == '__main__':
  print(run(sys.stdin.read()))
