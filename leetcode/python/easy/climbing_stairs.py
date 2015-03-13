# https://leetcode.com/problems/climbing-stairs/
# Climbing Stairs
class Solution:
    def climbStairsWithCapture(self,n,capture):
        if n in capture.keys():
            return capture[n]
        x=0
        for possible in [1,2]:
            if n-possible >0:
                x = x + self.climbStairsWithCapture(n-possible,capture)
            elif n-possible < 0:
                continue
            else:
                x = x + 1
        capture[n] = x
        return x

    def climbStairs(self, n):
        capture=dict()
        return self.climbStairsWithCapture(n,capture)