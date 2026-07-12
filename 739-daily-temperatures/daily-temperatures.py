class Solution(object):
    def dailyTemperatures(self, temperatures):
        total_days = len(temperatures)
        ans = [0] * total_days
        stack = []
        for current_day in range(total_days):
            current_temp = temperatures[current_day]
            while stack and current_temp > temperatures[stack[-1]]:
                past_day = stack.pop()                
                ans[past_day] = current_day - past_day

            stack.append(current_day)
            
        return ans