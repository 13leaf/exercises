#https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        rhead = ListNode(0)
        rhead.next = head
        prev = rhead
        current = rhead.next
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return rhead.next