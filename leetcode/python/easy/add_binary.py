#https://leetcode.com/problems/add-binary/
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        isCarry=False
        maxLength=max(len(a),len(b))
        a=a.rjust(maxLength,'0')[::-1]
        b=b.rjust(maxLength,'0')[::-1]
        c=[]
        ascii0=ord('0')
        for i in range(maxLength):
            x=(ord(a[i])-ascii0+ord(b[i])-ascii0)
            if isCarry:
                x=x+1
            if x >= 2:
                x=x-2
                isCarry=True
            else:
                isCarry=False
            c.append(str(x))
        if isCarry:
            c.append('1')
        c.reverse()
        return ''.join(c)
s=Solution()
print s.addBinary('11','1')