# Gray Code
# https://oj.leetcode.com/problems/gray-code/
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n <=0: return [0]
        binary=['']
        for i in range(n):
            next=[x+y for x in ['0'] for y in binary]+[x+y for x in ['1'] for y in reversed(binary)]
            binary=next
        return map(lambda x:int(x,2),binary)
s=Solution()
print s.grayCode(2)
print s.grayCode(3)
print s.grayCode(4)