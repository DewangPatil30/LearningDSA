def intersetPoint(head1,head2):
    p, q = head1, head2
    
    while p != q:
        if not p: p = head2
        if not q: q = head1
        
        p = p.next
        q = q.next
        
    return p.data
  
  #GFG: https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/0/#
