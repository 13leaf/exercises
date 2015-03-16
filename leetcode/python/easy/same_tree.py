from __init__ import *
# Same Tree
#https://leetcode.com/problems/same-tree/
class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        if self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        else:
            return False