class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        
        for i in tokens:
            if i in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                elif i == "/":
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(i))
                
        return stack[0]