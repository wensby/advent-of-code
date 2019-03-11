def run(input):
  return len(input) - (2 * len(input.replace('(', '')))

if __name__ == "__main__":
  print(run(input()))