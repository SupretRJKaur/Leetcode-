class Solution:

    def hammingWeight(self,n):
        count = 0
        while n > 0:
            n = n & (n - 1)  # Drops the lowest set bit (1)
            count += 1
        return count