class Solution:

    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit):
            visit.add((r, c))

            if r + 1 < rows and (r + 1, c) not in visit and heights[r + 1][c] >= heights[r][c]:
                dfs(r + 1, c, visit)

            if r - 1 >= 0 and (r - 1, c) not in visit and heights[r - 1][c] >= heights[r][c]:
                dfs(r - 1, c, visit)

            if c + 1 < cols and (r, c + 1) not in visit and heights[r][c + 1] >= heights[r][c]:
                dfs(r, c + 1, visit)

            if c - 1 >= 0 and (r, c - 1) not in visit and heights[r][c - 1] >= heights[r][c]:
                dfs(r, c - 1, visit)

        for r in range(rows):
            dfs(r, 0, pac)
        for c in range(cols):
            dfs(0, c, pac)

        for r in range(rows):
            dfs(r, cols - 1, atl)
        for c in range(cols):
            dfs(rows - 1, c, atl)

        return [[r, c] for r in range(rows) for c in range(cols) if (r, c) in pac and (r, c) in atl]