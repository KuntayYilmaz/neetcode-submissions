# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = None
        carry = 0
        while l1 or l2:
        
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_val = (v1 + v2 + carry)
            if sum_val > 9:
                carry = 1
            else:
                carry = 0
            sum_val = sum_val % 10

            if curr:
                temp = ListNode(sum_val)
                curr.next = temp
                curr = temp
            else:
                curr = ListNode(sum_val)
                head = curr
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry:
            temp = ListNode(1)
            curr.next = temp
            curr = temp

        return head


            
