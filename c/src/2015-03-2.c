#include <stdio.h>

typedef struct Coordinates {
  int x, y;
} Coordinates;

typedef struct Santa {
  Coordinates coordinates;
} Santa;

void move(Santa *santa, char order) {
  if (order == '>') {
    santa->coordinates.x++;
  }
  if (order == '<') {
    santa->coordinates.x--;
  }
  if (order == 'v') {
    santa->coordinates.y++;
  }
  if (order == '^') {
    santa->coordinates.y--;
  }
}

int givePresent(int grid[][200], Coordinates coordinates) {
  int y = coordinates.y + 100;
  int x = coordinates.x + 100;
  grid[y][x]++;
  return grid[y][x] - 1;
}

int main(void) {
  char c; 
  int grid[200][200] = {0};
  Santa santas[2];
  Santa *currentSanta;
  int happyHouseholds = 0;

  santas[0].coordinates = (Coordinates){0, 0};
  santas[1].coordinates = (Coordinates){0, 0};
  currentSanta = &(santas[0]);
  if (!givePresent(grid, currentSanta->coordinates)) {
    happyHouseholds++;
  }
  while ((c = getchar()) != EOF) {
    move(currentSanta, c);
    if (!givePresent(grid, currentSanta->coordinates)) {
      happyHouseholds++;
    }
    currentSanta = currentSanta == &(santas[0]) ? &(santas[1]) : &(santas[0]);
  }
  
  printf("%d\n", happyHouseholds);
}
