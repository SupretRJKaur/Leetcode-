class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        N1, N2 = len(nums1), len(nums2)
        if N1 > N2:
            return self.findMedianSortedArrays(nums2, nums1)
            
        lb, ub = 0, N1 * 2
        
        while lb <= ub:
            mid1 = (lb + ub) // 2  
            mid2 = N1 + N2 - mid1     
            L1 = float('-inf') if mid1 == 0 else nums1[(mid1 - 1) // 2]
            L2 = float('-inf') if mid2 == 0 else nums2[(mid2 - 1) // 2]
            R1 = float('inf') if mid1 == N1 * 2 else nums1[mid1 // 2]
            R2 = float('inf') if mid2 == N2 * 2 else nums2[mid2 // 2]
            if L1 > R2:
                ub = mid1 - 1 
            elif L2 > R1:
                lb = mid1 + 1  
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0
        return -1