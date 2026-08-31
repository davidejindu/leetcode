"""
need two stacks a normal stack and min
if min[-1] < the val getting pushed then just push the value on top

"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if self.min_stack:
            minn = self.min_stack[-1]
            if val < minn:
                self.min_stack.append(val)
            else:
                self.min_stack.append(minn) 

        else:
            self.min_stack.append(val)   

        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()