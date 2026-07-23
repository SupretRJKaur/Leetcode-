class Solution(object):
    def calculate(self, s):
        s = s.replace(" ", "") + "+"
        stack = []
        j = 0    
        i = "+"  
        
        for char in s:
            if char.isdigit():
                j = (j * 10) + int(char)
            else:
                if i == "+":
                    stack.append(j)
                elif i == "-":
                    stack.append(-j)
                elif i == "*":
                    stack.append(stack.pop() * j)
                elif i == "/":
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(-prev // j))
                    else:
                        stack.append(prev // j)
                i = char
                j = 0
        return sum(stack)