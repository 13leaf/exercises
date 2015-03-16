#pascal's triangle II
#https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex):
        if rowIndex < 0: return []
        if rowIndex == 0: return [1]
        pre=self.getRow(rowIndex-1)
        list=[1]
        for i in range(rowIndex/2):
            list.append(pre[i]+pre[i+1])
        list.extend(list[::-1] if rowIndex%2 == 1 else list[-2::-1])
        return list
s=Solution()
print s.getRow(1)