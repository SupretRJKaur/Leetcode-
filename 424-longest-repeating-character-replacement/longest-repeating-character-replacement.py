class Solution(object):
    def characterReplacement(self, s, k):
        counts = {}
        max_count = 0
        i = 0
        ans = 0 
        
        for j in range(len(s)):
            char = s[j]
            counts[char] = counts.get(char, 0) + 1
            
            # Keep track of the most frequent character in our current window
            max_count = max(max_count, counts[char])
            
            # If the number of characters we need to replace is greater than k
            while (j - i + 1) - max_count > k:
                counts[s[i]] -= 1
                i += 1  
            ans = max(ans, j - i + 1)
            
        return ans