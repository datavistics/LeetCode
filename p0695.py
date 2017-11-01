import timeit


def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid:
        return 0

    import sys
    sys.setcheckinterval(100000)

    num_rows = len(grid)
    num_cols = len(grid[0])

    def dfs(r, c):
        if 0 <= r < num_rows and 0 <= c < num_cols and grid[r][c]:
            grid[r][c] = 0
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        return 0

    largest = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j]:
                largest = max(largest, dfs(i, j))

    return largest


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

# maxAreaOfIsland(grid)


result = timeit.repeat(lambda: maxAreaOfIsland(grid), number=10000)

from pprint import pprint
pprint(result)
