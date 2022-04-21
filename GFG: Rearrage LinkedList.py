"""
    Approaches:
            
            1. TC: O(2N)  SC:O(N):
                a. iterate over list and count nodes-1 and mark last node as end
                b. if count % 2 == 1: count // 2 + 1 else count // 2
                c. cur = head
                
                d. while count:     (1) end.next = cur.next (2) cur.next = cur.next.next (3) end.next.next = None
                    cur = cur.next, end = end.next count -= 1
                return Head    
                
            2. TC: O(N) SC: O(1): Merging 2 Lists 
                a. oddHead, evenHead = head, head.next
                    odd, even = head, head.next
                    
                b. while even and even.next:
                    odd.next = odd.next.next
                    even.next = even.next.next
                    
                    odd = odd.next same with even
                
                c. odd.next = evenHead
                return head
                
                
GFG: https://practice.geeksforgeeks.org/problems/rearrange-a-linked-list/1/#
YT: https://www.youtube.com/watch?v=YE9ggKeHeK0
"""
############### Approach 1 ###########
class Solution:    
    def rearrangeEvenOdd(self, head):
        #code here
        if not head or not head.next or not head.next.next: 
            return head
        
        count = 0
        end = head
        
        while end.next:
            count += 1
            end = end.next
            
            
        if count % 2: count = (count // 2) + 1
        else: count = count // 2
            
            
        cur = head
        while count:
            end.next = cur.next
            cur.next = cur.next.next
            end.next.next = None
            
            cur = cur.next
            end = end.next
            
            count -= 1
            
        return head
    
#################### Approach 2 ##########
class Solution:    
    def rearrangeEvenOdd(self, head):
        #code here
        if not head or not head.next or not head.next.next: 
            return head
        
        oh, eh = head, head.next
        o, e = head, head.next
        
        while e and e.next:
            
            o.next = o.next.next
            e.next = e.next.next
            
            o = o.next
            e = e.next
            
        o.next = eh
        
        return head
    
