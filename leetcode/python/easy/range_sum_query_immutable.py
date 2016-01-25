#https://leetcode.com/problems/range-sum-query-immutable/
from collections import defaultdict

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.cacheRange = defaultdict(dict)
        self.cacheRange[0] = nums
        maxStep = len(str(len(nums)))
        for i in range(1,maxStep):
            span = 10 ** i
            preSpan = 10 ** (i-1)
            for j in range(0,len(nums),span):
                self.cacheRange[i][j] = 0
                for k in range(j,j + span,preSpan):
                    if k + 1 < len(nums):
                        self.cacheRange[i][j] += self.cacheRange[i-1][k]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        s = 0
        while True:
            maxStep = min(len(str(i)),len(str(j-i)))
            if j-i<10:
                s += sum(self.nums[i:j+1])
                break
            for step in range(maxStep-1,-1,-1):
                if i < j and i % (10 ** step) == 0:
                    s += self.cacheRange[step][i]
                    i += 10 ** step
                    break
        return s

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
