# https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self.eles=[]
        self.minEles=[]
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.eles) == 0 or self.minEles[-1]>=x:
            self.minEles.append(x)
        self.eles.append(x)

    # @return nothing
    def pop(self):
        if self.minEles[-1] == self.eles[-1]:
            self.minEles.pop()
        self.eles.pop()

    # @return an integer
    def top(self):
        return self.eles[-1]

    # @return an integer
    def getMin(self):
        return self.minEles[-1]

stack=MinStack()
stack.push(-3)
print stack.top()
print stack.getMin()