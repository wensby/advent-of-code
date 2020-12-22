import sys

def solve(input):
  memory = {}
  mask = None
  for line in input.splitlines():
    if line.startswith('mask'):
      mask = line.split(' = ')[1]
    else:
      address = int(line[4:].split(']')[0])
      unmasked_value_dec = int(line.split(' = ')[1])
      unmasked_value_bin = bin(unmasked_value_dec)[2:].zfill(36)
      masked_value_bin = ''.join([unmasked_value_bin[i] if mask[i] == 'X' else mask[i] for i in range(36)])
      masked_value_dec = int(masked_value_bin, 2) 
      memory[address] = masked_value_dec
  return sum(memory.values())

if __name__ == '__main__':
  print(solve(sys.stdin.read()))
