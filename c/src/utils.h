#ifndef UTILS_H
#define UTILS_H

struct RowReader {
  char* buffer;
  char* pointer;
  int read_character;
};

void initialize_row_reader(struct RowReader *reader, size_t size);
void free_row_reader(struct RowReader *reader);
int read_row(struct RowReader *reader);
int read_int_row(struct RowReader *reader, int *result);

#endif
