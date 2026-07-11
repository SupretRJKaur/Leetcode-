class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False  
        t_list = list(t)
        for char in s:
            if char in t_list:
                t_list.remove(char)
            else:
                return False        
        return True