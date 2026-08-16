class Solution(object):

    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        def backtrack(start, remaining_target, path):
            if remaining_target == 0:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > remaining_target:
                    break
                path.append(num)
                backtrack(i, remaining_target - num, path)
                path.pop()
        backtrack(0, target, [])
        return res