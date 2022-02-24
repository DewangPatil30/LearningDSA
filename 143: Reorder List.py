class Solution:
    def split(self, node):      #Return the mid of the List
        slow, fast = node, node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def reverse(self, node):    #Reverse the second half of the list
        prev = None
        curr = node
        nxt = node.next
        while nxt:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
            
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return head   # Handling Edge cases
        elif not head.next.next.next: 
            head.next.val, head.next.next.val = head.next.next.val, head.next.val
            return head
        
        n = self.split(head)      #Here n = mid of list
        newnode = n.next
        n.next = None             # Break list into two halfs
        newnode = self.reverse(newnode)
        ntemp = newnode
        temp = head
        
        while temp and ntemp:
            nxt = temp.next
            newnxt = ntemp.next   #Store the nexts of both half's node
            
            temp.next = ntemp
            ntemp.next = nxt      # Merge the list by order First --> Second
            
            temp = nxt
            ntemp = newnxt
