"""
# Minefield Generator

Generates a new minefield map based on desired size and the amount of mines
you want.

Output:
    X 2 1 0
    2 X 1 0
    1 1 1 0
    0 0 0 0
"""
import random

MINE_CHAR = 'X'
NEIGHBOURS = ((-1,-1), (-1,0), (-1,1),
              (0,-1),          (0,1),
              (1,-1),  (1,0),  (1,1))

def gen_minefield(size, mines):
    minefield = [[0]*size for _ in range(size)]

    for _ in range(mines):
        while True:
            x = random.randrange(0, size)
            y = random.randrange(0, size)
            if not minefield[x][y] == MINE_CHAR:
                minefield[x][y] = MINE_CHAR
                break

        for dx, dy in NEIGHBOURS:
            if 0 <= x+dx <= size-1 and 0 <= y+dy <= size-1:
                if not minefield[x+dx][y+dy] == MINE_CHAR:
                    minefield[x+dx][y+dy] += 1

    return minefield

if __name__ == '__main__':
    minefield = gen_minefield(size=4, mines=2)
    for row in minefield:
        print(*row)
