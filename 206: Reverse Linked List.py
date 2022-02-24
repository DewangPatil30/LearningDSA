# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ########## Iterative Solution ########
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        nxt = head.next
        
        while nxt:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev
        
        ########## Recursive Solution ########
        
        def reverse(prev, curr):
                    
            if not curr:
                return prev

            tail = reverse(curr, curr.next)
            curr.next = prev
            
            return tail
        
        return reverse(None, head)
