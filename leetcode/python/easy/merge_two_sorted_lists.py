from __init__ import *
#https://leetcode.com/problems/merge-two-sorted-lists/
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # ensure l2 insert after l1's head
        if l1.val > l2.val:
            l1,l2 = l2,l1
        pl1=l1
        pl2=l2
        while pl2 is not None:
            pl1Next = pl1.next
            if pl1Next is None:
                pl1.next=pl2
                break
            if pl2.val < pl1Next.val:
                pl2Next = pl2.next
                pl1.next=pl2
                pl2.next=pl1Next
                pl2=pl2Next
                continue
            pl1=pl1Next
        return l1

l1=ListNode(-10)
l1.next=ListNode(-9)
l1.next.next=ListNode(-6)
l1.next.next.next=ListNode(-4)
l1.next.next.next.next=ListNode(1)
l1.next.next.next.next.next=ListNode(9)
l1.next.next.next.next.next.next=ListNode(9)
l2=ListNode(-5)
l2.next=ListNode(-3)
l2.next.next=ListNode(0)
l2.next.next.next=ListNode(7)
l2.next.next.next.next=ListNode(8)
l2.next.next.next.next.next=ListNode(8)

s=Solution()
l=s.mergeTwoLists(l1,l2)
#