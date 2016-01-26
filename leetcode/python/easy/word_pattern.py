#https://leetcode.com/problems/word-pattern/
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        tokens = str.split()
        if len(tokens) != len(pattern):
            return False
        tokenWords = {}
        for i,k in enumerate(pattern):
            if k not in tokenWords:
                tokenWords[k] = tokens[i]
            elif tokenWords[k] != tokens[i]:
                return False
        return len(tokenWords) == len(set(tokenWords.values()))