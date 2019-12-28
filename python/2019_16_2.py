import sys
from functools import lru_cache

def run(input):
  signal = list(map(int, input)) * 10000
  offset = int(''.join(map(str, signal[:7])))
  return find_message(signal, offset, 8)

def find_message(signal, offset, message_length):
  offsetted_signal = signal[offset:]
  for phase in range(100):
    accumulated = 0
    for i in reversed(range(len(offsetted_signal))):
      accumulated = offsetted_signal[i] = (offsetted_signal[i] + accumulated) % 10
  return ''.join(map(str, offsetted_signal))[:message_length]

if __name__ == '__main__':
  print(run(sys.stdin.read().splitlines()[0]))
