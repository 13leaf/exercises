#https://leetcode.com/problems/implement-strstr/
# strStr
class Solution:
    def strStr(self,haystack,needle):
        needleLen=len(needle)
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+needleLen] == needle:
                return i
        return -1
s=Solution()
print s.strStr("","")
print s.strStr("012356123","123")
