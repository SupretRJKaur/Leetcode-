class Solution:

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def backtrack(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0" or (r, c) in visited:
                return
            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                next_r = r + dr
                next_c = c + dc
                backtrack(next_r, next_c)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    backtrack(r, c)
        return islands