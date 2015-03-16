from __init__ import *
#https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Minimum depth of tree
class Solution:
    def _minDepth(self,node,depth):
        if node.left is None and node.right is None:
            return depth
        if node.left is not None and node.right is not None:
            return min(self._minDepth(node.left,depth+1),self._minDepth(node.right,depth+1))
        elif node.left is None:
            return self._minDepth(node.right,depth+1)
        else:
            return self._minDepth(node.left,depth+1)

    def minDepth(self, root):
        if root is None:
            return 0
        return self._minDepth(root,1)

root=TreeNode(1)
root.left=TreeNode(2)
print Solution().minDepth(root)