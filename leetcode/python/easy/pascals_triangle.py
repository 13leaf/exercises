#pascal's triangle
#https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows):
        if numRows < 1: return []
        if numRows == 1: return [[1]]
        list=self.generate(numRows-1)
        pre=list[-1]
        t=[1]
        for i in range((numRows+1)/2-1):
            t.append(pre[i]+pre[i+1])
        t.extend(t[::-1] if numRows%2 == 0 else t[-2::-1])
        list.append(t)
        return list

s=Solution()
print s.generate(10)