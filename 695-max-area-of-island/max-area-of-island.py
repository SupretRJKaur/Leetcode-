class Solution:

    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def backtrack(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            # Sink the cell so we never visit it again
            grid[r][c] = 0

            # 1 (current cell) + sum of all 4 directions
            return (
                1
                + backtrack(r + 1, c)
                + backtrack(r - 1, c)
                + backtrack(r, c + 1)
                + backtrack(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, backtrack(r, c))

        return max_area