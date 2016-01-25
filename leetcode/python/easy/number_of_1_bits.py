#https://leetcode.com/problems/number-of-1-bits/
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        hammingWeight = 0
        while n > 0:
            x = n % 2
            if x == 1:
                hammingWeight += 1
            n = (n-x) / 2
        return hammingWeight