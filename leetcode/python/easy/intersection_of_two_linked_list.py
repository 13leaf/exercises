# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        (nodeA, nodeB) = (headA, headB)
        while nodeA != nodeB:
            if not nodeA or not nodeB:
                return None
            while nodeB and nodeA and nodeA.val < nodeB.val:
                nodeA = nodeA.next
            while nodeA and nodeB and nodeB.val < nodeA.val:
                nodeB = nodeB.next
        return nodeA