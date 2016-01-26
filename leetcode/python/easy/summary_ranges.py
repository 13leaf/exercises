#https://leetcode.com/problems/summary-ranges/
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ret = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            end = start
            while i < n and end == nums[i]:
                i += 1
                end += 1
            end = end-1
            if start == end:
                ret.append("{}".format(start))
            else:
                ret.append("{}->{}".format(start,end))
        return ret