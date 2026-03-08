
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast=head
        slow= head
        while fast!=None and fast.next!=None:
            fast= fast.next.next
            slow=slow.next
        curr= slow.next
        slow.next= None

        next=None
        prev=None

        while curr!=None:
            next= curr.next
            curr.next= prev
            prev= curr
            curr=next
        first= head
        second= prev

        while second!=None:
            temp1=first.next
            temp2= second.next
            first.next=second
            second.next= temp1
            first=temp1
            second=temp2

