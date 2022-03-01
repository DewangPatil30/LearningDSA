class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # TO FIND THE MID OF LL
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # REVERSE AFTER MID
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # CHECK PALINDROME
        while head and prev:
            if head.val != prev.val: return False
            head = head.next
            prev = prev.next
            
        return True
      
      # TC: O(n) SC: O(1)
