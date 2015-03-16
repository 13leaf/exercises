from __init__ import *
#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# level order traversal II
class Solution:
    def _levelOrder(self,nodeList,outList):
        l=[]
        nextNodeList=[]
        for node in nodeList:
            if node is None:
                continue
            l.append(node.val)
            nextNodeList.extend([node.left,node.right])
        if len(l) == 0:
            return
        outList.append(l)
        self._levelOrder(nextNodeList,outList)

    def levelOrderBottom(self, root):
        outList=[]
        self._levelOrder([root],outList)
        outList.reverse()
        return outList
