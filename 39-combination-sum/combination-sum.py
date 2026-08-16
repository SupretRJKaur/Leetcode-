class Solution(object):

    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, t, p):
            if t == 0:
                res.append(list(p))
                return
            if i >= len(candidates) or t < 0:
                return
            p.append(candidates[i])
            dfs(i, t - candidates[i], p)
            p.pop()
            dfs(i + 1, t, p)

        dfs(0, target, [])
        return res