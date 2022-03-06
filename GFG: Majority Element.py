"""
Approaches :-
    1. Use DefaultDict to count freq of each ele return if any ele freq is > n//2: 
        tc = O(n) sc = O(n)
        
    2. Moorie's Voting Algorithm: eg arr = [3,1,2,3,3]
        a. Take 1st ele as ele and count = 1
        b. loop in range i = 1, i < n:
        c. agar arr[i] ele ke eq h to count++ krdo nhi to count--
        d. agar count = 0 ho gya to ele = arr[i], count = 1-------ele or count ko reassign krdo
        e. last m ele ki freq nikalo agar ele ki freq n//2 se badi h to return ele else return -1
        
        tc = O(n) sc = O(1)
        
    GFG: https://practice.geeksforgeeks.org/problems/majority-element-1587115620/0/#
    YT: https://www.youtube.com/watch?v=YXywKwT9EKA
"""


def majorityElement(self, arr, n):
        
        c = 1
        ele = arr[0]
        for i in range(1, n):
            if arr[i] == ele:
                c += 1
            else: c -= 1
            
            if c == 0:
                ele = arr[i]
                c = 1
                
        c = 0
        for i in range(n):
            if arr[i] == ele:
                c += 1
            if c > n//2: return ele
        
        return -1
