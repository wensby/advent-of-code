import sys

def run(input):
  input_lines = input.splitlines()
  bus_ids = [int(id) if id != 'x' else None for id in input_lines[1].split(',')]
  bus_id_by_offset = {o: bus_ids[o] for o in range(0, len(bus_ids)) if bus_ids[o]}
  return find_aligned_timestamp(bus_id_by_offset)

def find_aligned_timestamp(bus_id_by_offset):
  remaining_offsets = sorted(list(bus_id_by_offset.keys()))
  cycle = 1
  t = 0
  while remaining_offsets:
    target_offset = remaining_offsets.pop(0)
    target_bus_id = bus_id_by_offset[target_offset]
    # find next working minute
    while (t+target_offset) % target_bus_id != 0:
      t += cycle
    # we found a minute that works for this bus, and all previous buses
    if remaining_offsets:
      # now find next workable cycle
      next_cycle = cycle
      t_temp = t + cycle
      while (t_temp+target_offset) % target_bus_id != 0:
        next_cycle += cycle
        t_temp += cycle
      # we found the next cycle to use
      cycle = next_cycle
  return t

"""
(0,2) + (1,3) = (4,6)

     0 1       0 1 2 3 4
time 2 3     | x x x x 6

1    . .       . . . . .
2    D . <-    . . . . .
3    . D       . . . . .
4    D .       . . . . .
5    . .       . . . . .
6    D D       . . . . D
7    . .
8    D . <-
9    . D
10   D .
11   . .
12   D D
13   . .
14   D . <-
15   . D

(0,2) + (2,3) = (2,6)

     0 1 2       0 1 2
time 2 x 3     | x x 6

1    . . .       . . . . .
2    D . .       . . . . .
3    . . D       . . . . .
4    D . . <-    . . . . .
5    . . .       . . . . .
6    D . D       . . D . .
7    . . .
8    D . .
9    . . D
10   D . . <-
11   . . .
12   D . D
13   . . .
14   D . .
15   . . D
"""


if __name__ == '__main__':
  print(run(sys.stdin.read()))
