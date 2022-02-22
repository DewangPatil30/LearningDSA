# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sta, stb = [], []
        
        while l1 or l2:
            if l1:
                sta.append(l1.val)
                l1 = l1.next
            if l2:
                stb.append(l2.val)
                l2 = l2.next
                
        rem = 0
        nhead = None
        
        while sta != [] or stb != []:
            total = 0
            if sta != []:
                total += sta.pop()
            if stb != []:
                total += stb.pop()
            
            total += rem
            rem = 0
            
            if total > 9:
                total, rem = total % 10, total // 10
            
            newnode = ListNode(total)
            if nhead is None:
                nhead = newnode
            else:
                newnode.next = nhead
                nhead = newnode
                
        if rem > 0:
            n = ListNode(rem)
            n.next = nhead
            nhead = n
            
        return nhead
            
            
            
                
