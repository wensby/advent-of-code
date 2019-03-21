#include <stdio.h>
#include <stdlib.h>

struct Present {
  int l, w, h;
};

int getLine(char* buffer)
{
  int i;
  int c;

  i = 0;
  while ((c = getchar()) != '\n') {
    if (c == EOF) {
      return 0;
    }
    else {
      buffer[i++] = c;
    }
  }
  buffer[i] = '\0';
  return 1;
}

void parsePresent(struct Present *present, char *line)
{
  char c;
  char *start;
  char *end;
  int l, w, h;

  start = line;
  l = strtol(start, &end, 10);
  start = end+1;
  w = strtol(start, &end, 10);
  start = end+1;
  h = strtol(start, &end, 10);
  present->l = l;
  present->w = w;
  present->h = h;
}

int smallestSide(struct Present *present)
{
  int lw;
  int lh;
  int hw;

  lw = present->l * present->w;
  lh = present->l * present->h;
  hw = present->h * present->w;
  if (lw <= lh && lw <= hw) {
    return lw;
  }
  else if (lh <= lw && lh <= hw) {
    return lh;
  }
  else {
    return hw;
  }
}

int main(void)
{
  char lineBuffer[20];
  int lineRead;
  struct Present present;
  int wrapping;

  wrapping = 0;
  while ((lineRead = getLine(lineBuffer)) == 1) {
    parsePresent(&present, lineBuffer);
    wrapping += smallestSide(&present) 
        + (2 * present.l * present.h) 
        + (2 * present.w * present.l) 
        + (2 * present.w * present.h);
  }

  printf("%d\n", wrapping);
}
