#https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, A, elem):
        A[:] = filter(lambda x: x != elem, A)
        # A.sort(lambda x,y:abs(y-elem)-abs(x-elem))
        return len(A)