#!/usr/bin/python3
"""
Island Perimeter Problem
"""


def island_perimeter(grid: list) -> int:
    """
    Calculate the perimeter of an island represented in a 2D grid.

    Args:
        grid: A 2D list where 1 represents land and 0 represents water.

    Returns:
        The perimeter of the island.
    """
    min_h, max_h = 0, len(grid)
    min_w, max_w = 0, len(grid[0])
    perimeter = 0

    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == 0:
                continue

            # Right
            if col_idx + 1 < max_w:
                if row[col_idx + 1] == 0:
                    perimeter += 1  # Land surrounded by water
            else:
                perimeter += 1  # Last column

            # Left
            if col_idx - 1 >= min_w:
                if row[col_idx - 1] == 0:
                    perimeter += 1  # Land surrounded by water
            else:
                perimeter += 1  # First column

            # Up
            if row_idx - 1 >= min_h:
                if grid[row_idx - 1][col_idx] == 0:
                    perimeter += 1  # Land surrounded by water
            else:
                perimeter += 1  # First row

            # Down
            if row_idx + 1 < max_h:
                if grid[row_idx + 1][col_idx] == 0:
                    perimeter += 1  # Land surrounded by water
            else:
                perimeter += 1  # Last row

    return perimeter
