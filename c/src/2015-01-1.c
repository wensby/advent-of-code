#include <stdio.h>

int main(void)
{
  int floor = 0;
  int c;
  while ((c = getchar()) != EOF) {
    if (c == '(') {
      floor += 1;
    }
    else if (c == ')') {
      floor -= 1;
    }
  }
  printf("%d\n", floor);
}
