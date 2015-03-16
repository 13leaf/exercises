# Two Sum
# https://oj.leetcode.com/problems/two-sum/
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        m=dict()
        for i in range(len(num)):
            if not num[i] in m:
                m[num[i]]=[]
            m[num[i]].append(i+1)
        for x in num:
            if m.has_key(target-x):
                if x*2==target and len(m[target-x]) == 1:
                    continue
                return (m[x][0],m[target-x][-1])
s=Solution()
num=[3,2,4]
print s.twoSum(num,6)