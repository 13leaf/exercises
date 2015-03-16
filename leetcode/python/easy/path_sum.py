from __init__ import *
#path sum
#https://leetcode.com/problems/path-sum/
class Solution:
    def _hasPathSum(self,node,sum,expect):
        sum = sum + node.val
        if node.left is None and node.right is None:
            return sum == expect
        if node.left is not None and node.right is not None:
            return self._hasPathSum(node.left,sum,expect) or self._hasPathSum(node.right,sum,expect)
        elif node.left is None:
            return self._hasPathSum(node.right,sum,expect)
        else:
            return self._hasPathSum(node.left,sum,expect)

    def hasPathSum(self, root, sum):
        if root is None:
            return False
        return self._hasPathSum(root,0,sum)

root=TreeNode(1)
print Solution().hasPathSum(root,0)