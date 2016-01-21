#https://leetcode.com/problems/odd-even-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddList = ListNode(0)
        evenList = ListNode(0)
        oddNode = oddList
        evenNode = evenList
        node = head
        isOdd = True
        while node:
            if isOdd:
                oddNode.next = node
                oddNode = node
            else:
                evenNode.next = node
                evenNode = node
            isOdd = not isOdd
            node = node.next
        #concat two list
        oddNode.next = evenList.next
        evenNode.next = None
        return oddList.next
