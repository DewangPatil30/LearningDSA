"""
  Approach:
  
            1. TC: O(N) SC: O(1)
                a. join end to head to make circular ll
                b. cur = cur.next for 0 to k-1
                c. head = cur.next and cur.next = None
                return head

GFG: https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1/?page=2&company[]=Amazon&sortBy=submissions#
"""

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if not head or not head.next or k == 0: return head
        
        cur = head
        while cur.next: cur = cur.next
            
        cur.next = head
        cur = head
        
        for i in range(k-1):
            cur = cur.next

        head = cur.next
        cur.next = None
        
        return head
    
    
