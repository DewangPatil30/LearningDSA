"""
  For i = 0 to n-1            
    If 'i' is even
       arr[i] += arr[max_index] % max_element * max_element 
       max_index--     
    ELSE // if 'i' is odd
       arr[i] +=  arr[min_index] % max_element * max_element
       min_index++
       
  How does expression "arr[i] += arr[max_index] % max_element * max_element" work ? 
  
    The purpose of this expression is to store two elements at index arr[i]. arr[max_index] is stored as multiplier and "arr[i]" is stored as remainder. 
    For example in {1 2 3 4 5 6 7 8 9}, max_element is 10 and we store 91 at index 0. With 91, we can get original element as 91%10 and new element as 91/10.
    Below implementation of above idea:
  
  GFG: https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately-1587115620/1#
 
"""

def rearrange(self,arr, n): 
        max_idx = n - 1
        min_idx = 0
    
        # Store maximum element of array
        max_elem = arr[n-1] + 1
    
        # Traverse array elements
        for i in range(0, n) :
    
            # At even index : we have to put maximum element
            if i % 2 == 0 :
                arr[i] += (arr[max_idx] % max_elem ) * max_elem
                max_idx -= 1
    
            # At odd index : we have to put minimum element
            else :
                arr[i] += (arr[min_idx] % max_elem ) * max_elem
                min_idx += 1
    
        # array elements back to it's original form
        for i in range(0, n) :
            arr[i] = arr[i] // max_elem 
            

            
            
