#https://leetcode.com/problems/add-digits/
class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        x = num
        ret = 0
        while True:
            ret += x%10
            x=x/10
            if x==0:
                if ret>9:
                    x=ret
                    ret=0
                else:
                    break
        return ret

# O(1)
class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if num == 0:
            return 0
        else:
            return (num-1) % 9 + 1

s=Solution()
for i in range(1,301):
    print i,s.addDigits(i)
