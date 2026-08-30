class Solution:

    def cloneGraph(self, node):
        if not node:
            return None

        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]

            # 1. Create copy of current node
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # 2. Recursively clone neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)