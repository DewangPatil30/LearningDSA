"""
2 Approaches: 
    
    1. for each i travase arr[i+1:] and find next greater if present: tc = O(N^2) sc = O(1)
    
    2. Use Stack: tc = O(N) sc = O(N):- 
            a. create index stack = [0]
            b. travase from 1 to n and check if stack and arr[stack.top] < arr[i]
               so arr[stack.pop()] = arr[i] coz it will be its next greater 
            c. Continue b. till its condition is failed.... if failed than push i in stack
            d. when travasal is complete than put -1 on each index in stack coz for thoes indexes no greater ele 
               is present for thoes indexes
            
    GFG: https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1#
    YT: https://www.youtube.com/watch?v=sDKpIO2HGq0
"""
class Solution:
    def nextLargerElement(self,arr,n):
        st = [0]
        i = 1
        while i < n:
            if st and arr[st[-1]] < arr[i]:
                arr[st.pop()] = arr[i]
            else:
                st.append(i)
                i += 1
                
        while st:
            arr[st.pop()] = -1
            
        return arr
