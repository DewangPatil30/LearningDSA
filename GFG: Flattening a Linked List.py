"""
Approach:

  1. Create the dummy node and dummy.next = head
  2. Merge lists dummy and temp  till temp not None 
  3. update merge list each time in dummy.next
  4. Return dummy.next
  
 GFG: https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1#
"""
def flatten(head):
    def merge(a, b):
        dummy = Node(None)
        d = dummy
        
        while a and b:
            if a.data < b.data:
                d.bottom = Node(a.data)
                a = a.bottom
            else:
                d.bottom = Node(b.data)
                b = b.bottom
            d = d.bottom
        
        if a: d.bottom = a
        if b: d.bottom = b
          
        return dummy.bottom
        
    dummy = Node(None)
    d = dummy
    d.bottom = head
    
    temp = head.next
    while temp:
        d.bottom = merge(d.bottom, temp)
        temp = temp.next
    return d.bottom
  
