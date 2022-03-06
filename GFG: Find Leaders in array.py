"""
Use stack and traverse array from back 
if arr[i] {i=n-2, i>=0, i--} >= stack.top
stack.push(arr[i])

GFG: https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1#
"""

def leaders(self, arr, n):
        st = [arr[-1]]
        for i in range(n-2, -1, -1):
            if arr[i] >= st[-1]:
                st.append(arr[i])
                
        return st[::-1]
