#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct Box {
  int length;
  int width;
  int height;
};

int perimiter(int a, int b) {
  return 2 * (a + b);
}

int calc_ribbon(struct Box *box) {
  int lw = perimiter(box->length, box->width);
  int lh = perimiter(box->length, box->height);
  int wh = perimiter(box->width, box->height);
  int wrap = fmin(lw, fmin(lh, wh));
  return wrap + box->length * box->width * box->height;
}

struct Box * parsebox(char *line) {
  char *end;
  struct Box *box = malloc(sizeof(struct Box));
  box->length = strtol(line, &end, 10);
  box->width = strtol(++end, &end, 10);
  box->height = strtol(++end, NULL, 10);
  return box;
}

int main(void) { 
  int ribbon = 0;
  char *line = NULL;
  size_t len = 0;
  ssize_t nread;

  while ((nread = getline(&line, &len, stdin)) != -1) {
    struct Box *box = parsebox(line);
    ribbon += calc_ribbon(box);
    free(box);
  }

  printf("%d\n", ribbon);
}
