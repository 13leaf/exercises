#https://leetcode.com/problems/power-of-two/
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 2 and n % 2 == 0:
            n = n / 2
        if n == 1:
            return True
        return False