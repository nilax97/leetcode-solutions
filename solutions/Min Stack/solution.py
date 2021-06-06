class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.top1 = -1
        self.min = list()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if(len(self.stack)==1):
            self.min.append(x)
        else:
            self.min.append(min(self.min[self.top1],x))
        self.top1+=1
        

    def pop(self) -> None:
        self.stack.pop(self.top1)
        self.min.pop(self.top1)
        self.top1-=1
        

    def top(self) -> int:
        return self.stack[self.top1]

    def getMin(self) -> int:
        return self.min[self.top1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
