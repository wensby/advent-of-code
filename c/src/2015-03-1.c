#include <stdio.h>
#include <stdlib.h>

typedef struct Position {
  int x;
  int y;
} Position;

typedef struct Grid {
  int size;
  int **rows;
} Grid;

int givePresent(Grid *grid, Position *position) {
  Position gridPosition;
  int halfSize;

  halfSize = grid->size / 2;

  gridPosition = (Position){position->x + halfSize, position->y + halfSize};
  if (grid->rows[gridPosition.y] == NULL) {
    grid->rows[gridPosition.y] = malloc(grid->size * sizeof(int *));
    for (int i = 0; i < grid->size; i++) {
      grid->rows[gridPosition.y][gridPosition.x] = 0;
    }
  }
  grid->rows[gridPosition.y][gridPosition.x]++;
  return grid->rows[gridPosition.y][gridPosition.x] - 1;
}

void initializeGrid(Grid *grid, int size) {
  grid->size = size;
  grid->rows = malloc(size * sizeof(int *));
  for (int i = 0; i < size; i++) {
    grid->rows[i] = NULL;
  }
}

void freeGrid(Grid *grid) {
  for (int i = 0; i < grid->size; i++) {
    if (grid->rows[i] != NULL) {
      free(grid->rows[i]);
    }
  }
  free(grid->rows);
}

int main(void) {
  Grid grid;
  Position santaPosition;
  char c;
  int happyHouseholdCount;

  santaPosition = (Position){0, 0};
  happyHouseholdCount = 0;
  initializeGrid(&grid, 100);

  if (!givePresent(&grid, &santaPosition)) {
    happyHouseholdCount++;
  }
  while ((c = getchar()) != EOF) {
    if (c == '>') {
      santaPosition.x++;
    }
    if (c == '<') {
      santaPosition.x--;
    }
    if (c == 'v') {
      santaPosition.y++;
    }
    if (c == '^') {
      santaPosition.y--;
    }
    if (!givePresent(&grid, &santaPosition)) {
      happyHouseholdCount++;
    }
  }
  printf("%d\n", happyHouseholdCount);
  freeGrid(&grid);
}
