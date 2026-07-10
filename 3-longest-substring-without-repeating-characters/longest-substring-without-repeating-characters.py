class Solution(object):
    def lengthOfLongestSubstring(self, s):
        w = set()  
        i = 0         
        ans = 0     
    
        for j in range(len(s)):
            while s[j] in w:
                w.remove(s[i])
                i += 1    
            w.add(s[j])
            ans = max(ans, j - i + 1)
        return ans