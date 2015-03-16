from __init__ import *
#https://leetcode.com/problems/symmetric-tree/
#Symmetric Tree

class Solution:
    def isSymmetricList(self,nodeList):
        valList=[]
        for node in nodeList:
            if node is None:
                valList.append('#')
            else:
                valList.append(node.val)
        #iterate ending: len 0 or fully none
        if len(valList) == 0 or set(valList) == set('#'):
            return True
        if valList != list(reversed(valList)):
            return False
        nextNodeList=[]
        for node in nodeList:
            if node is None:
                continue
            else:
                nextNodeList.append(node.left)
                nextNodeList.append(node.right)
        return self.isSymmetricList(nextNodeList)

    def isSymmetric(self, root):
        return self.isSymmetricList([root])


root=TreeNode(1)
root.left=TreeNode(-57)
root.right=TreeNode(-57)
root.left.right=TreeNode(67)
root.right.left=TreeNode(67)
root.left.right.right=TreeNode(-97)
root.right.left.left=TreeNode(-97)

s=Solution()
print s.isSymmetric(root)