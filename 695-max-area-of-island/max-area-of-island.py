class Solution:

    def maxAreaOfIsland(self, grid):
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def backtrack(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            area = 1  # Count current land cell

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                next_r = r + dr
                next_c = c + dc
                area += backtrack(next_r, next_c)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_area = backtrack(r, c)
                    max_area = max(max_area, current_area)

        return max_area