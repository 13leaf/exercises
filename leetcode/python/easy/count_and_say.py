#https://leetcode.com/problems/count-and-say/
# countAndSay
class Solution:
    def countAndSay(self,n):
        if n==1: return '1'
        pre=self.countAndSay(n-1)
        list=[]
        count=0
        last=pre[0]
        for c in pre:
            if last == c:
                count=count+1
            else:
                list.append(str(count))
                list.append(last)
                last=c
                count=1
        list.append(str(count))
        list.append(c)
        return ''.join(list)

s=Solution()
print s.countAndSay(6)