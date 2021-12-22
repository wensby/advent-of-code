#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

int read_next_depth(struct RowReader *reader, int *depth)
{
  return read_int_row(reader, depth);
}

int count_depth_increases()
{
  int count = 0;
  int prev_depth;
  int depth;
  struct RowReader reader;
  initialize_row_reader(&reader, 5);

  read_next_depth(&reader, &prev_depth);
  while ((read_next_depth(&reader, &depth))) {
    if (depth > prev_depth) {
      count++;
    }
    prev_depth = depth;
  }

  free_row_reader(&reader);
  return count;
}

int main(void)
{
  printf("%d\n", count_depth_increases());
}
