#https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i,x in enumerate(nums[1:],1):
            if x == nums[i-1]:
                return True
        return False