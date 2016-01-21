#https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def shift(nums,pos):
            for i in range(pos,len(nums)-1):
                nums[i] = nums[i+1]

        lastZero = len(nums) -1
        nonZero = 0
        while nonZero < lastZero:
            if nums[nonZero] == 0:
                shift(nums,nonZero)
                nums[lastZero] = 0
                lastZero -= 1
            else:
                nonZero += 1