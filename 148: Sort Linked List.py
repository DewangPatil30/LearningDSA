# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def split(node):
            
            slow, fast = node, node
            
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                
            return slow
            
        def merge(left, right):
            dummy = curr = ListNode()
            infMax = float('inf')
            
            while left or right:
                lv, rv = left.val if left else infMax, right.val if right else infMax
                
                if lv < rv:
                    curr.next = left
                    curr = curr.next
                    left = left.next
                else:
                    curr.next = right
                    curr = curr.next
                    right = right.next
                    
            return dummy.next
            
            
            
        def sort(node):
            
            mid = split(node)
            newnode = mid.next
            mid.next = None
            
            l = sort(node)
            r = sort(newnode)
            
            return merge(l, r)
            
        
        return sort(head)
        
        
