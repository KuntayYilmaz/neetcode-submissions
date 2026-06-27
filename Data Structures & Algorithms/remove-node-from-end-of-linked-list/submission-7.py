# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L, R = head, head
        while n > 0:
            R = R.next
            n -= 1

        if not R:
            return head.next

        while R:
            prev_L = L
            L = L.next
            R = R.next

        prev_L.next = L.next
        
        return head





        