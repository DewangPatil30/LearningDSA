"""
  Approach: eg head = [1,2,3,4,5], k = 2
      1. Create a dummy node with next = head
      2. get the kth node 
      3. create 2 ptrs groupPrev, groupAfter for prev node before group and and after kth node
      4. if not kth node just return dummy.next
      5. else reverse groups in k 
      6. update the group prev
      
      TC:O(K * N) 
      
  LeetCode 25: https://leetcode.com/problems/reverse-nodes-in-k-group/
  NeetCode: https://www.youtube.com/watch?v=1UOPsfP85V4
  Explaination: https://takeuforward.org/data-structure/reverse-linked-list-in-groups-of-size-k/ 
"""

class Solution:
    def getkth(self, curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head
        
        dummy = ListNode(next=head)
        groupPrev = dummy
        
        while True:
            kth = self.getkth(groupPrev.next, k-1)
            if not kth: 
                break
                
            groupAfter = kth.next
            prev, curr = groupAfter, groupPrev.next
            while curr != groupAfter:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next
            
            
