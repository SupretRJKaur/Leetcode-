class Solution:
    def maxSubArray(self, nums):
        n=len(nums)
        total=0
        max_total=float("-inf")
        for i in range (n):
            total=total+nums[i]
            max_total=max(max_total,total)
            if total<0:
                total=0
        return max_total