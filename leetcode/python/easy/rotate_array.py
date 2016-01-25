#https://leetcode.com/problems/rotate-array/
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        kList = nums[-k:]
        for i,x in enumerate(nums[:-k]):
            nums[i+k] = x
        for j,x in enumerate(kList):
            nums[j] = x