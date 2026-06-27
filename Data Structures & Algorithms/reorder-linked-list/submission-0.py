# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        F = head
        S = head
        while F and F.next:
            F = F.next.next
            S = S.next

        
        prev = S
        curr = S.next
        S.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        L = head
        R = prev

        while L != R:
            temp = L.next
            L.next = R
            L = temp
            if L != R:
                temp = R.next
                R.next = L
                R = temp

        


    
        