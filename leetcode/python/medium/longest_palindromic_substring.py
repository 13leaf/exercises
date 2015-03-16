# Longest Palindromic substring
# https://oj.leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def isPalindrome(self,s,i,j):
        substr=s[i:j+1]
        return substr == substr[::-1]

    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        indexMap=dict()
        for i,v in enumerate(s):
            if not v in indexMap:
                indexMap[v]=[]
            indexMap[v].append(i)
        longestLen=0
        longestBound=(0,0)
        for c,l in indexMap.items():
            for i in range(len(l)):
                for j in range(len(l)-1,i-1,-1):
                    if l[j]-l[i]>longestLen and self.isPalindrome(s,l[i],l[j]):
                        longestLen=l[j]-l[i]
                        longestBound=(l[i],l[j])
        return s[longestBound[0]:longestBound[1]+1]
s=Solution()
print s.longestPalindrome('bb')
print s.longestPalindrome('abccba')
print s.longestPalindrome('aba')
print s.longestPalindrome('dabccbaff')
print s.longestPalindrome('a')
print timeit.timeit('test()','from __main__ import test',number=10)