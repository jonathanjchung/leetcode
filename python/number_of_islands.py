# attempt one
# i believe this is a dfs or bfs problem but i'm not brushed up on them at the moment
# used hints for this problem and looked up dfs algorithm for refresher
from collections import deque


def numIslands(grid: list[list[str]]) -> int:
    result = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == '1':
                result += 1
                helper(grid, visited, i, j)
    return result


def helper(grid, visited, x, y):
    visited.add((x, y))
    if x > 0 and (x - 1, y) not in visited:
        if grid[x - 1][y] == '1':
            helper(grid, visited, x - 1, y)
    if x + 1 < len(grid) and (x + 1, y) not in visited:
        if grid[x + 1][y] == '1':
            helper(grid, visited, x + 1, y)
    if y > 0 and (x, y - 1) not in visited:
        if grid[x][y - 1] == '1':
            helper(grid, visited, x, y - 1)
    if y + 1 < len(grid[0]) and (x, y + 1) not in visited:
        if grid[x][y + 1] == '1':
            helper(grid, visited, x, y + 1)


# O(m*n)
# this one uses bfs approach instead of recursive dfs
def attempt_two(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    def bfs(r, c):
        search_queue = deque()
        visited.add((r, c))
        search_queue.append((r, c))
        while search_queue:
            row, col = search_queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in directions:
                r, c = row + dx, col + dy
                if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                    search_queue.append((r, c))
                    visited.add((r, c))

    result = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    for x in range(rows):
        for y in range(cols):
            if (x, y) not in visited and grid[x][y] == '1':
                bfs(x, y)
                result += 1
    return result
