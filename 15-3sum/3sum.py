class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            # ULTRA OPTIMIZATION: If the first number is > 0, 
            # no positive numbers ahead can sum up to 0. Stop completely!
            if nums[i] > 0:
                break
                
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            L, R = i + 1, n - 1
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                
                if total == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]: 
                        L += 1
                    while L < R and nums[R] == nums[R + 1]: 
                        R -= 1
                elif total < 0:
                    L += 1
                else:
                    R -= 1
                    
        return res
        