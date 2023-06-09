class MinStack:

    def __init__(self):
        # initialize a stack list and min value list for later user
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:
        # This adds the new value onto the stack, then check if the new value added is smaller that the value already on the min stack. if it is then it is appended and if not the current min val is appended again
        # we append the value onto the stack
        self.stack.append(val)
        # compare our current value with the most recent value added to our min stack list
        if self.min:
            val = min(val,self.min[-1])
        # append that value onto our list
        self.min.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()