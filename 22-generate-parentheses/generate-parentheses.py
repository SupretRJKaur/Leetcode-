class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def gp(current_str, open, close):
            if len(current_str) == 2 * n:
                ans.append(current_str)
                return
            if open < n:
                gp(current_str + "(", open + 1, close)
            if close < open:
                gp(current_str + ")", open, close + 1)
        gp("", 0, 0)
        return ans