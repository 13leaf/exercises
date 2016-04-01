from __init__ import *
#https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recursiveBinaryTreePaths(self,root,result):
        path.append(str(root.val))
        if root.left is None and root.right is None:
            result.append('->'.join(path))
            return
        if root.left:
            self.recursiveBinaryTreePaths(root.left,result,path[:])
        if root.right:
            self.recursiveBinaryTreePaths(root.right,result,path[:])

    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root is None:
            return []
        result=[]
        self.recursiveBinaryTreePaths(root,result,[])
        return result

root=TreeNode(1)
root.right=TreeNode(2)
s=Solution()
print s.binaryTreePaths(root)
