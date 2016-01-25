#https://leetcode.com/problems/happy-number/
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        chars = list(str(n))
        while len(chars) > 1:
            n = sum(map(lambda c: int(c) ** 2,chars))
            chars = list(str(n))
        return '17'.find(chars[0]) != -1