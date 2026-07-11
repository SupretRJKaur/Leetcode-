class Solution(object):
    def maxProduct(self, nums):
        length = len(nums)
        result = nums[0]
        prefix = 0
        suffix = 0
        for i in range(length):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[length - 1 - i]
            if prefix > result: result = prefix
            if suffix > result: result = suffix
        return result