#https://leetcode.com/problems/string-to-integer-atoi/
# atoi
class Solution:
    def atoi(self,str):
        str=str.strip()
        positive=True
        if len(str)>0:
            positive=str[0] != '-'
            if str[0] in ['-','+']: str=str[1:]
        r=0
        for cstr in str:
            c=ord(cstr)
            if c>=ord('0') and c<=ord('9'):
                r=r*10+(c-ord('0'))
            else:
                break
        #lazy to do overflow detect work
        return min(r,2147483647) if positive else max(-r,-2147483648)

s=Solution()
print s.atoi("  010")
print s.atoi("+123")
print s.atoi(" 445")
print s.atoi("-566.324")
print s.atoi("21474836499")
print s.atoi("-21474836498")