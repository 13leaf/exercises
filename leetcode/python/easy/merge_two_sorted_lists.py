from __init__ import *
#https://leetcode.com/problems/merge-two-sorted-lists/
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head=new ListNode(0);
        ListNode iter=head;
        while(true){
            if(l1==null){
                iter.next=l2;
                break;
            }
            if(l2==null){
                iter.next=l1;
                break;
            }
            if(l1.val<l2.val){
                iter.next=l1;
                l1=l1.next;
            }else{
                iter.next=l2;
                l2=l2.next;
            }
            iter=iter.next;
        }
        return head.next;
    }
}

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