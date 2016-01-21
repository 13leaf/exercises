#https://leetcode.com/problems/excel-sheet-column-number/
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column = 0
        for char in s:
            pad = ord(char) - ord('A') + 1
            column = column * 26 + pad
        return column