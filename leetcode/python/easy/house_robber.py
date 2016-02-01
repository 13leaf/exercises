#https://leetcode.com/problems/house-robber/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dpCache = {}
        def bestRob(nums,i):
            if i < 0:
                return 0
            elif i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0],nums[1])
            elif i in dpCache:
                return dpCache[i]
            dpCache[i] = max(bestRob(nums,i-2)+nums[i],bestRob(nums,i-1))
            return dpCache[i]

        return bestRob(nums,len(nums)-1)