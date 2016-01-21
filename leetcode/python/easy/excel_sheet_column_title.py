#https://leetcode.com/problems/excel-sheet-column-title/
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ""
        level = 0
        while n > 0:
            pad = (n-1) % 26
            title += chr(ord('A') + pad)
            n = (n-pad) / 26
        return title[::-1]
