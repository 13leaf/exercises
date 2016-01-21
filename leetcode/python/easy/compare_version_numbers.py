#https://leetcode.com/problems/compare-version-numbers/
from itertools import izip_longest
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int,version1.split('.'))
        v2 = map(int,version2.split('.'))
        for x1,x2 in izip_longest(v1,v2):
            x1 = x1 or 0
            x2 = x2 or 0
            if x1 > x2:
                return 1
            elif x1 < x2:
                return -1
        return 0
