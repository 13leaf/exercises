from __init__ import *
# remove duplicates from sorted list
#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        pre=head
        current=head.next
        while current is not None:
            if pre.val != current.val:
                pre.next=current
                pre=current
            elif current.next is None:
                pre.next=None
            current=current.next
        return head


s=Solution()
l=ListNode(1)
l.next=ListNode(1)
l.next.next=ListNode(2)
l.next.next.next=ListNode(3)
l.next.next.next.next=ListNode(3)
l=s.deleteDuplicates(l)
