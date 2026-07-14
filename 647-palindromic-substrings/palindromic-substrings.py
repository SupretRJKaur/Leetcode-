class Solution(object):
    def countSubstrings(self, s):
        ans = 0
        n = len(s)
        
        for i in range(n):
            # Case 1: Odd length palindromes (Center is s[i])
            L, R = i, i
            while L >= 0 and R < n and s[L] == s[R]:
                ans += 1
                L -= 1  # Expand left
                R += 1  # Expand right
                
            # Case 2: Even length palindromes (Center is between s[i] and s[i+1])
            L, R = i, i + 1
            while L >= 0 and R < n and s[L] == s[R]:
                ans += 1
                L -= 1  # Expand left
                R += 1  # Expand right
                
        return ans