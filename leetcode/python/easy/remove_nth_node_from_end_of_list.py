from __init__ import *
# remove nth node from end of list
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution:
    def removeNthFromEnd(self, head, n):
        length = 0
        iter=head
        while iter is not None:
            length=length+1
            iter=iter.next
        pos=length-n
        if pos < 0:
            return head
        if pos == 0:
            return head.next
        iter=head
        for i in range(pos-1):
            iter=iter.next
        iter.next=iter.next.next
        return head

l=ListNode(1)
l.next=ListNode(2)
s=Solution()
l=s.removeNthFromEnd(l,2)