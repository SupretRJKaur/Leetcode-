class Solution(object):

    def permute(self, nums):
        res = []

        def dfs(p):
            if len(p) == len(nums):
                res.append(list(p))
                return

            for num in nums:
                if num in p:
                    continue

                p.append(num)
                dfs(p)
                p.pop()

        dfs([])
        return res