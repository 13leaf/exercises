#https://leetcode.com/problems/ugly-number/
class Solution:
    # @param {integer} num
    # @return {boolean}
    def isUgly(self, num):
        if num == 0:
            return True
        while True:
            if num % 2 == 0:
                num = num / 2
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num / 5
            else:
                break
        return num == 1
s = Solution()
print s.isUgly(-2147483648)
