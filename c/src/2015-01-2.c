#include <stdio.h>

int main(void)
{
  int floor;
  int c;
  int i;

  floor = 0;
  i = 0;
  while ((c = getchar()) != EOF) {
    if (c == '(') {
      floor++;
    }
    else if (c == ')') {
      floor--;
    }
    i++;
    if (floor < 0) {
      printf("%d\n", i);
      break;
    }
  }
}
