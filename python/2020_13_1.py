import sys

def run(input):
  input_lines = input.splitlines()
  earliest_timestamp = int(input_lines[0])
  bus_ids = [int(id) for id in input_lines[1].split(',') if id != 'x']
  upcoming_bus, diff = find_upcoming_bus(earliest_timestamp, bus_ids)
  return upcoming_bus * diff

def find_upcoming_bus(earliest_timestamp, bus_ids):
  closest_diff = None
  closest_bus_id = None
  for bus_id in bus_ids:
    diff = bus_id - (earliest_timestamp % bus_id)
    if not closest_diff or diff < closest_diff:
      closest_diff = diff
      closest_bus_id = bus_id
  return closest_bus_id, closest_diff

if __name__ == '__main__':
  print(run(sys.stdin.read()))
