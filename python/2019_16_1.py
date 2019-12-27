import sys

base_pattern = [0, 1, 0, -1]


def run(input):
  return ''.join(map(str, fft(input, phases=100)[0:8]))

def fft(signal, phases=1):
  signal = list(map(int, signal))
  for i in range(phases):
    signal = fft_once(signal)
  return ''.join(map(str, signal))

def fft_once(signal):
  return list(map(lambda x: apply_pattern(signal, x), range(len(signal))))

def apply_pattern(signal, position):
  def pattern_generator(position):
    i = position
    while True:
      i += 1
      yield base_pattern[int(i // (1+position)) % 4]
  generator = pattern_generator(position)
  sum = 0
  for signal_index in range(position, len(signal)):
    next_pattern_value = next(generator)
    sum += signal[signal_index] * next_pattern_value
  return abs(sum) % 10

if __name__ == '__main__':
  print(run(sys.stdin.read().splitlines()[0]))
