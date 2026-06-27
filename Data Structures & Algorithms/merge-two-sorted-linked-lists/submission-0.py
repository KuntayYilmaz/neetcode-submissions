# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p_l1, p_l2 = list1, list2
        if not p_l1:
            return list2
        if not p_l2:
            return list1

        if list1.val < list2.val:
            p_l1 = list1.next 
            curr = list1
            new_head = list1
        else:
            p_l2 = list2.next
            curr = list2
            new_head = list2
        
        while p_l1 or p_l2:
            if not p_l1:
                temp = p_l2
                p_l2 = temp.next
                curr.next = temp
                curr = temp
            elif not p_l2:
                temp = p_l1
                p_l1 = temp.next
                curr.next = temp
                curr = temp 
            elif p_l1.val < p_l2.val:
                temp = p_l1
                p_l1 = temp.next
                curr.next = temp
                curr = temp 
            else:
                temp = p_l2
                p_l2 = temp.next
                curr.next = temp
                curr = temp

        return new_head

            