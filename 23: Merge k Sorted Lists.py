# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def merge(self, la, lb):
          
        dummy = ListNode()
        curr = dummy
        while la and lb:
            if la.val < lb.val:
                curr.next = la
                la = la.next
            else:
                curr.next = lb
                lb = lb.next

            curr = curr.next

        if la: curr.next = la
        if lb: curr.next = lb

        return dummy.next
  
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) < 1:
            return None
        
        mlist = []
        
        while len(lists) > 1:
            mlist = []
            for i in range(0, len(lists), 2):
                la = lists[i]
                lb = lists[i+1] if i+1 < len(lists) else None
                
                mlist.append(self.merge(la, lb))
                
            lists = mlist
            
        return lists[0]
 
