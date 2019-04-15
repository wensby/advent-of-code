#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "md5.h"

int leadingZeroes(unsigned char * subject) {
  char first8[10];
  sprintf(first8, "%02x%02x%02x%02x", subject[0], subject[1], subject[2], subject[3]);
  for (int i = 0; i < 8; i++) {
    if (first8[i] != '0') {
      return i;
    }
  }
  return 10000;
}

int main(void) {
  MD5_CTX ctx;
  unsigned char result[100];

  char string[100];
  int number = 0;
  result[0] = 1;
  result[1] = 1;
  result[2] = 1;
  result[3] = 1;
  result[4] = 1;
  result[5] = 1;
  result[6] = 0;
  char input[20];

  char c;
  int ii = 0;
  while ((c = getchar()) != EOF) {
    input[ii] = c;
    if (c == '\n') {
      input[ii] = '\0';
    }
    ii++;
  }

  while (leadingZeroes(result) < 5) {
    sprintf(string, "%s%d", input, ++number);
    MD5_Init(&ctx);
    MD5_Update(&ctx, (const void *)string, strlen(string));
    MD5_Final(result, &ctx);
  }
  printf("%d\n", number);
}
