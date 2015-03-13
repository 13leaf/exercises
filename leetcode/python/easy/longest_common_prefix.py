#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        longestPrefix=[]
        minimumString=min(strs)
        for i in range(len(minimumString)):
            fullMatch=True
            for str in strs:
                if str[i]!=minimumString[i]:
                    fullMatch=False
                    break
            if fullMatch:
                longestPrefix.append(minimumString[i])
            else:
                break
        return ''.join(longestPrefix)
s=Solution()
print s.longestCommonPrefix(["abcd","abcefg","abcehhh"])
