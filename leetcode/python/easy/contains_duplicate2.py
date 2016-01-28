#https://leetcode.com/problems/contains-duplicate-ii/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dupDict = {}
        for i,x in enumerate(nums):
            if x not in dupDict:
                dupDict[x] = [i]
            else:
                dupDict[x].append(i)
        for v in dupDict.values():
            for i in range(len(v)):
                if i+1<len(v) and v[i+1] - v[i] <= k:
                    return True
        return False