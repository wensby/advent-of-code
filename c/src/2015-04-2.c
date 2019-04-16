#include <stdio.h>
#include <string.h>
#include "md5.h"

void readInput(char * buffer, size_t bufferSize) {
  char c;
  size_t i;
  for (i = 0; i < bufferSize; i++) {
    c = getchar();
    if (c == '\n' || c == EOF) {
      break;
    }
    else {
      buffer[i] = c;
    }
  }
  buffer[i] = '\0';
}

void hexify(unsigned char * hash, char * hex) {
  int i;
  char* ptr = hex;
  char* endofbuf = hex + 32;
  for (i = 0; i < 16; i++) {
    if (ptr + 5 < endofbuf) {
      ptr += sprintf(ptr, "%02x", hash[i]);
    }
  }
  ptr[0] = '\0';
}

void md5(char * data, char * hex) {
  MD5_CTX ctx;
  unsigned char hash[16];

  MD5_Init(&ctx);
  MD5_Update(&ctx, (const void *) data, strlen(data));
  MD5_Final(hash, &ctx);
  hexify(hash, hex);
}

int getLeadingZeroes(char * hash) {
  int i, length;
  for (i = 0, length = strlen(hash); i < length; i++) {
    if (hash[i] != '0') {
      break;
    }
  }
  return i;
}

int main(void) {
  char input[10], hash[32], data[20];
  int number, leadingZeroes;

  readInput(input, sizeof(input));
  number = leadingZeroes = 0;
  while (leadingZeroes < 6) {
    sprintf(data, "%s%d", input, ++number);
    md5(data, hash);
    leadingZeroes = getLeadingZeroes(hash);
  }

  printf("%d\n", number);
}
