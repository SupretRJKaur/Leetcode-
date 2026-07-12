class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1
        window = {}
        have = 0
        need = len(target)
        i = 0
        best_len = len(s) + 1
        start_idx = 0
        for j in range(len(s)):
            char = s[j]
            window[char] = window.get(char, 0) + 1
            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                size = j - i + 1               
                if size < best_len:
                    best_len = size
                    start_idx = i
                left_char = s[i]
                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1

                i += 1

        if best_len > len(s):
            return ""
        return s[start_idx : start_idx + best_len]