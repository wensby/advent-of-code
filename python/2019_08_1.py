import sys

def run(input):
  layers = parse_layers(input)
  layer_with_fewest_zeroes = get_layer_with_fewest_zeroes(layers)
  one_count = layer_with_fewest_zeroes.count('1')
  two_count = layer_with_fewest_zeroes.count('2')
  return one_count * two_count

def parse_layers(input):
  layer_digits = 25 * 6
  layer_count = len(input) // layer_digits
  return [stringpart(input, layer_digits, i) for i in range(layer_count)]

def stringpart(string, part_size, index):
  return string[index*part_size:(index*part_size)+part_size]

def get_layer_with_fewest_zeroes(layers):
  layers_copy = layers.copy()
  layers_copy.sort(key=lambda x: x.count('0'))
  return layers_copy[0]

if __name__ == '__main__':
  print(run(sys.stdin.read()))
