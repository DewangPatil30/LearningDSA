# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
              
            newlist = ListNode()
            newlistptr = newlist

            while l1 and l2:
                if l1.val <= l2.val:
                    newlistptr.next = l1
                    l1 = l1.next
                else:
                    newlistptr.next = l2
                    l2 = l2.next
                newlistptr = newlistptr.next
            if l1 != None:
                newlistptr.next = l1
            else:
                newlistptr.next = l2
            return newlist.next
        NewList = ListNode()
        
############### Rucursive ####################
		
        def Merge(NewList,node1,node2):

                if node1 == None and node2 == None:
                    return

                if node1 == None and node2 != None:
                    return node2

                if node2 == None and node1 != None:
                    return node1

                if node1.val <= node2.val:
                    NewList = node1
                    NewList.next = Merge(NewList, node1.next,node2)

                if node1.val > node2.val:
                    NewList = node2
                    NewList.next = Merge(NewList, node1,node2.next)

                return NewList
            
