def run(input):
  floor = 0
  index = 0
  for c in input:
    index = index + 1
    floor = floor + 1 if c == '(' else floor - 1
    if floor < 0:
      return index
  return index

if __name__ == "__main__":
  print(run(input()))