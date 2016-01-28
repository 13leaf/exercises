#https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = n
        x = 0
        while t > 0:
            t = t / 5
            x += t
        return x