from __init__ import *
#https://leetcode.com/problems/balanced-binary-tree/
# balance tree
class Solution:
    def _maxDepth(self,node,depth):
        if node.left is None and node.right is None:
            return depth
        ldepth,rdepth=depth,depth
        if node.left is not None:
            ldepth=self._maxDepth(node.left,depth+1)
        if node.right is not None:
            rdepth=self._maxDepth(node.right,depth+1)
        if abs(ldepth-rdepth)>1:
            raise StopIteration()
        return ldepth if ldepth>rdepth else rdepth

    def isBalanced(self, root):
        try:
            if root is None:
                return True
            self._maxDepth(root,1)
            return True
        except StopIteration:
            return False

root=TreeNode(1)
root.right=TreeNode(2)
root.right.right=TreeNode(3)
s=Solution()
print s.isBalanced(root)