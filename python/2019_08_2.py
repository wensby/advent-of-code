import sys

def run(input):
  dimensions = 25, 6
  layers = parse_layers(input, dimensions)
  return render(layers, dimensions)

def parse_layers(input, dimensions):
  layer_digits = dimensions[0] * dimensions[1]
  layer_count = len(input) // layer_digits
  return [stringpart(input, layer_digits, i) for i in range(layer_count)]

def stringpart(string, part_size, index):
  return string[index*part_size:(index*part_size)+part_size]

def render(layers, dimensions):
  final = [' ']*len(layers[0])
  for layer in layers[::-1]:
    for i in range(len(layer)):
      digit = layer[i]
      if digit in '01':
        final[i] = '█' if digit == '0' else ' '
  rows = [stringpart(''.join(final), dimensions[0], row) for row in range(dimensions[1])]
  return '\n'.join(rows)

if __name__ == '__main__':
  print(run(sys.stdin.read()))
