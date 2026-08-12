class Solution(object):

    def subsets(self, nums):
        res = []

        def dfs(i, p):
            res.append(list(p))
            for j in range(i, len(nums)):
                p.append(nums[j])
                dfs(j + 1, p)  
                p.pop() 
        dfs(0, [])
        return res