# Integer to Roman
# https://oj.leetcode.com/problems/integer-to-roman/
class Solution:
    # @return a string
    def intToRoman(self, num):
        symbolMap={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        maxFloor=1000
        ret=[]
        floor=maxFloor
        while num > 0:
            if num >= floor:
                x = num/floor
                if x < 4:
                    ret.extend(symbolMap[floor]*x)
                elif x==4:
                    ret.extend(symbolMap[floor]+symbolMap[floor*5])
                elif x<9:
                    ret.extend(symbolMap[floor*5]+symbolMap[floor]*(x-5))
                elif x==9:
                    ret.extend(symbolMap[floor]+symbolMap[floor*10])
                num=num-x*floor
            floor = floor/10
        return ''.join(ret)
s=Solution()
print s.intToRoman(9)