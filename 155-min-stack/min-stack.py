class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            top_pair = self.stack[-1]
            old_min = top_pair[1]
            
            if val < old_min:
                new_min = val
            else:
                new_min = old_min
                
            self.stack.append((val, new_min))

    def pop(self):
        self.stack.pop()

    def top(self):
        top_pair = self.stack[-1]
        return top_pair[0]

    def getMin(self):
        top_pair = self.stack[-1]
        return top_pair[1]