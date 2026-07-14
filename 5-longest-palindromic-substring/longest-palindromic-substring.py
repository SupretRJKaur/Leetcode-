class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        ans = ""
        if n == 0:
            return ans
        if n == 1:
            return s
        for i in range(n):
            curr1 = self.checkPalindrome(s, i, i, n)
            curr2 = self.checkPalindrome(s, i, i + 1, n)       
            if len(curr1) > len(ans):
                ans = curr1
            if len(curr2) > len(ans):
                ans = curr2 
        return ans
    def checkPalindrome(self, s, p1, p2, n):
        curr = ""     
        while p1 >= 0 and p2 < n and s[p1] == s[p2]:
            curr = s[p1 : p2 + 1]
            p1 -= 1
            p2 += 1        
        return curr