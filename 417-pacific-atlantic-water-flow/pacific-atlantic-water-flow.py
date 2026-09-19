class Solution:

    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pac = set()
        atl = set()

        def backtrack(r, c, visit, prev_height):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if (r, c) in visit or heights[r][c] < prev_height:
                return

            visit.add((r, c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                backtrack(r + dr, c + dc, visit, heights[r][c])

        for c in range(cols):
            backtrack(0, c, pac, heights[0][c])
            backtrack(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            backtrack(r, 0, pac, heights[r][0])
            backtrack(r, cols - 1, atl, heights[r][cols - 1])

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])

        return result