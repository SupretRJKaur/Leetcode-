class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols =len(grid[0])
        islands = 0
        def backtrack(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                backtrack(r + dr, c + dc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    backtrack(r, c) 
        return islands