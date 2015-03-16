from __init__ import *
#https://leetcode.com/problems/maximum-depth-of-binary-tree/
# maximum depth of tree
class Solution:
    def _maxDepth(self,node,depth):
        if node.left is None and node.right is None:
            return depth
        if node.left is not None and node.right is not None:
            return max(self._maxDepth(node.left,depth+1),self._maxDepth(node.right,depth+1))
        elif node.left is None:
            return self._maxDepth(node.right,depth+1)
        else:
            return self._maxDepth(node.left,depth+1)

    def maxDepth(self, root):
        if root is None:
            return 0
        return self._maxDepth(root,1)