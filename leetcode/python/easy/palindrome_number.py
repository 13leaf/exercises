#https://leetcode.com/problems/palindrome-number/
#palindrome number
class Solution:
    def reverse(self, x):
        r=0
        positive=x>0
        if not positive:
            x=-x
        while x > 0:
            #check overflow
            if r>214748364:
                return 0
            r=r*10+x%10
            x=x/10
        return r * (1 if positive else  -1)

    def isPalindrome(self, x):
        if x<0:
            return False
        t=x
        tail = t % 10
        while t>=10:
            t=t/10
        if t != tail:
            return False
        return self.reverse(x) == x

s=Solution()
print s.isPalindrome(1001)
print s.isPalindrome(12321)
print s.isPalindrome(-123)
print s.isPalindrome(-121)
print s.isPalindrome(-2147447412)