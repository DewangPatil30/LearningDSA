# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        ########## ACTUAL SOL ###########
        
        temp = head
        i = 0
        
        while temp:
            i += 1
            temp = temp.next
            
        d = i - n + 1
        i = 0
        prev = None
        
        temp = head
        while temp:
            i += 1
            if i == d:
                if prev:
                    prev.next = temp.next
                else:
                    head = temp.next
                    
            prev = temp
            temp = temp.next
            
        return head

        ######### ONE GO ###########
        
        dummy = ListNode(next=head)
        
        slow, fast = dummy, dummy
        for i in range(n+1):

            fast = fast.next
            
        
                        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
