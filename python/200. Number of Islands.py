from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):

            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for drow, dcol in directions:
                    r, c = row + drow, col + dcol
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands