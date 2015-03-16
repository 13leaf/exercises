#https://leetcode.com/problems/valid-palindrome/
#Valid Palindrome
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s=filter(lambda x:x.isalpha() or x.isdigit(),s).lower()
        return s == s[::-1]

s=Solution()
print s.isPalindrome('A man, a plan, a canal: Panama')
print s.isPalindrome('race a car')
print s.isPalindrome('')