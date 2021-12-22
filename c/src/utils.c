#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

void initialize_row_reader(struct RowReader *reader, size_t size)
{
  (*reader).buffer = (char *) malloc(size);
}

void free_row_reader(struct RowReader *reader)
{
  free((*reader).buffer);
}

int read_row(struct RowReader *reader)
{
  (*reader).pointer = (*reader).buffer;
  while (((*reader).read_character = getchar()) != EOF) {
    if ((*reader).read_character != '\n') {
      *(*reader).pointer = (*reader).read_character;
      (*reader).pointer++;
    }
    else {
      *(*reader).pointer = '\0';
      return 1;
    }
  }
  return 0;
}

int read_int_row(struct RowReader *reader, int *result)
{
  if (read_row(reader)) {
    *result = atoi((*reader).buffer);
    return 1;
  }
  return 0;
}
