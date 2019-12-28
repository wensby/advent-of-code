import sys
from functools import lru_cache

base_pattern = [0, 1, 0, -1]

def run(input):
  signal = tuple(map(int, input))
  return find_first_8(signal)

def find_first_8(signal):
  digits = []
  for i in range(8):
    digits.append(reverse_fft(signal, i, 100))
    print(digits[-1])
  return ''.join(map(str, digits))

@lru_cache(maxsize=None)
def reverse_fft(signal, position, phase):
  if phase == 0:
    return signal[position]
  result = 0
  for i, f in get_sign_by_index(len(signal), position).items():
    result += reverse_fft(signal, i, phase-1) * f
  return abs(result) % 10

@lru_cache(maxsize=None)
def get_sign_by_index(length, position):
  sign_by_index = {}
  for i  in range(length):
    factor = base_pattern[int((i+1) // (1+position)) % 4]
    if factor != 0:
      sign_by_index[i] = factor
  return sign_by_index

if __name__ == '__main__':
  print(run(sys.stdin.read().splitlines()[0]))
