#https://leetcode.com/problems/isomorphic-strings/
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def compilePattern(s):
            containChars = {}
            i = 0
            pattern = []
            for x in s:
                if x not in containChars:
                    containChars[x] = i
                    i += 1
                pattern.append(containChars[x])
            return pattern
        return compilePattern(s) == compilePattern(t)