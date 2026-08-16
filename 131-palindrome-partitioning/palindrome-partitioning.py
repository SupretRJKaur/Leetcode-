class Solution:
    def partition(self, s):
        res = []
        
        def backtrack(remaining_str, current_partition):
            if not remaining_str:
                res.append(current_partition)
                return
            for i in range(1, len(remaining_str) + 1):
                prefix = remaining_str[:i]
                suffix = remaining_str[i:]
                if prefix == prefix[::-1]:
                    backtrack(suffix, current_partition + [prefix])
        backtrack(s, [])
        return res
