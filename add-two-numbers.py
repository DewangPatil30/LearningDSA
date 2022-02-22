# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        t1, t2 = l1, l2
        carry = 0
        newHead = ListNode(-1)
        temp = newHead
        
        while t1 or t2:
            total = 0
            
            if t1:
                total += t1.val
                t1 = t1.next
            if t2:
                total += t2.val
                t2 = t2.next
            

            total += carry
            
            if total > 9:
                carry, total = total // 10, total % 10
            else:
                carry = 0
            
            if temp.val == -1:
                temp.val = total
            else:
                temp.next = ListNode(total)
                temp = temp.next

        if carry:
            temp.next = ListNode(carry)
            
        return newHead
            
                
                
            
