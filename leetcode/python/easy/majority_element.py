#https://leetcode.com/problems/majority-element/
from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequenceDict = defaultdict(int)
        majoritySize = len(nums) / 2
        for x in nums:
            frequenceDict[x] += 1
            if frequenceDict[x] > majoritySize:
                return x