class Solution(object):
    def checkInclusion(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        
        # If s1 is longer than s2, a permutation cannot exist
        if n1 > n2:
            return False
            
        # Step 1: Create the target frequency dictionary for s1
        count1 = {}
        for char in s1:
            count1[char] = count1.get(char, 0) + 1
            
        # Step 2: Slide a fixed-size window across s2
        # i represents the starting index of our window
        for i in range(n2 - n1 + 1):
            # Create a fresh frequency dictionary for the current window
            count2 = {}
            
            # Count the characters in the current s2 window of size n1
            for j in range(n1):
                window_char = s2[i + j]
                count2[window_char] = count2.get(window_char, 0) + 1
                
            # If the current window matches s1 perfectly, we found it!
            if count1 == count2:
                return True
                
        return False