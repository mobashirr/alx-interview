#!/usr/bin/python3

'''
island perimeter problem
'''


from typing import List


def island_perimeter(self, grid: List[List[int]]) -> int:
    '''
    this function takes 2d array represent island sourounded by water

    grid:
        2d array represent the island -> 1 and the water -> 0
    Return:
        return the perimeter of the island

    '''
    min_h, max_h = (0, len(grid))
    min_h, max_h = (0, len(grid))
    min_h, max_h = (0, len(grid))
    min_w, max_w = (0, len(grid[0]))
    perimeter = 0

    for idx, row in enumerate(grid):
        for idx2, col in enumerate(row):
            if col == 0:
                continue
            elif col == 1:
                #   calulate the perimeter
                # right
                if (idx2 + 1) < max_w:
                    if row[idx2 + 1] == 0:
                        perimeter += 1  # case land souronded by water
                else:
                    perimeter += 1  # case last col

                # left
                if (idx2 - 1) >= min_w:
                    if row[idx2 - 1] == 0:
                        perimeter += 1   # case land souronded by water
                else:
                    perimeter += 1  # case first col is land

                # up
                if (idx - 1) >= min_h:
                    if grid[idx - 1][idx2] == 0:
                        perimeter += 1  # case land
                else:
                    perimeter += 1  # case first row

                # down
                if (idx + 1) < max_h:
                    if grid[idx + 1][idx2] == 0:
                        perimeter += 1  # case land
                else:
                    perimeter += 1  # case last row
    return perimeter
