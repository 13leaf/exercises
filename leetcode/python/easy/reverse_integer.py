# reverse integer
# https://leetcode.com/problems/reverse-integer/
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

s=Solution()
print s.reverse(-123)
print s.reverse(123)
print s.reverse(10100)
print s.reverse(100000000003)