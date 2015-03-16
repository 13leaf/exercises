#plusOne
#https://leetcode.com/problems/plus-one/
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry=False
        digits[-1]=digits[-1]+1
        for i in range(len(digits)-1,-1,-1):
            if carry:
                digits[i]=digits[i]+1
            if digits[i] == 10:
                carry = True
                digits[i] = 0
            else:
                carry =False
                break
        if carry:
            digits.insert(0,1)
        return digits

s=Solution()
digits=[8,9,9,9]
s.plusOne(digits)
print digits