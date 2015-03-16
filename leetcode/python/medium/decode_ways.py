# Decode Ways
# https://oj.leetcode.com/problems/decode-ways/
class Solution:
    def _numDecodings(self,s,captures):
        if len(s) == 0 or s[0] == '0':
            return 0
        if s in captures:
            return captures[s]
        num = self._numDecodings(s[1:],captures)
        if int(s[:2])<=26:
            num = num+self._numDecodings(s[2:],captures)
        captures[s]=num
        return captures[s]
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        captures=dict()
        for i in range(1,27):
            captures[str(i)]=1 if i<10 or i%10==0 else 2
        return self._numDecodings(s,captures)
s=Solution()
print s.numDecodings('012')