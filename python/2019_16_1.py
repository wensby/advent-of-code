import sys

base_pattern = [0, 1, 0, -1]


def run(input):
  return fft(input, phases=100)[0:8]

def fft(signal, phases=1):
  for i in range(phases):
    signal = ''.join(map(lambda x: apply_pattern(signal, x), range(len(signal))))
  return signal

def apply_pattern(signal, position):
  def pattern_generator(position):
    i = 0
    while True:
      i += 1
      yield base_pattern[int(i // (1+position)) % 4]
  generator = pattern_generator(position)
  sum = 0
  for signal_char in signal:
    digit = int(signal_char)
    next_pattern_value = next(generator)
    sum += digit * next_pattern_value
  return str(sum)[-1]

if __name__ == '__main__':
  print(run(sys.stdin.read().splitlines()[0]))
