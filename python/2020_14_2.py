import sys
import pprint
import time

def solve(input):
  memory = {}
  mask = None
  for line in input.splitlines():
    if line.startswith('mask'):
      mask = line.split(' = ')[1]
    else:
      encoded_address = int(line[4:].split(']')[0])
      value = int(line.split(' = ')[1])
      for address in get_floating_addresses(encoded_address, mask):
        memory[address] = value
  return sum(memory.values())

def get_floating_addresses(encoded_address, mask):
  decoded_address = decode_address(encoded_address, mask)
  return permutations(decoded_address)

def decode_address(address, mask):
  binary_address = bin(address)[2:].zfill(36)
  return ''.join([binary_address[i] if mask[i] == '0' else mask[i] for i in range(36)])

def permutations(float_address):
  float_positions = [i for i in range(len(float_address)) if float_address[i] == 'X']
  if not float_positions:
    return [float_address]
  result = []
  for varying_dec in range(2 ** len(float_positions)):
    varying_bin = bin(varying_dec)[2:].zfill(36)
    permutation = list(float_address)
    for i in range(len(float_positions)):
      permutation[float_positions[i]] = varying_bin[36-i-1]
    result.append(''.join(permutation))
  return result

if __name__ == '__main__':
  print(solve(sys.stdin.read()))
