#https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        rh = head
        node = head
        while node:
            next = node.next
            if next:
                next_node = next.next
                next.next = node
                node.next = rh
                rh = next
            else:
                next_node = None
                node.next = rh
                rh = node
            node = next_node
        head.next = None
        return rh

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        hashCode = 0
        i = 1
        while node:
            hashCode += node.val * i
            i += 1
            node = node.next
        rhashCode = 0
        rhead = rnode = self.reverseList(head)
        i = 1
        while rnode:
            rhashCode += rnode.val * i
            i += 1
            rnode = rnode.next
        return hashCode == rhashCode