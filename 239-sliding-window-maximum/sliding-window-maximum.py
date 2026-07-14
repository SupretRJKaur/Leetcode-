from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
            
        ans = []
        q = deque()  # Stores indices of elements
        
        for idx in range(len(nums)):
            # 1. Remove indices that have fallen out of the sliding window
            if q and q[0] < idx - k + 1:
                q.popleft()
                
            # 2. Remove smaller elements from the back (they can never be the max)
            while q and nums[q[-1]] < nums[idx]:
                q.pop()
                
            # 3. Add the current index to the back of the queue
            q.append(idx)
            
            # 4. Once our window is big enough (size k), record the max
            if idx >= k - 1:
                ans.append(nums[q[0]])
                
        return ans