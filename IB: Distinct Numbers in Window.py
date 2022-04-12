"""
  Approaches:
        1. Brute Force: O(N^2) O(N)
            create every subarray of window len and check for num of 
            distinct ele by using set
        
        2. Sliding Window: O(N) O(N)
            
            a. Take a queue q and map m
            b. same approach as Sliding Window maximum
            c. append each r in q and each arr[r] : r in map
            d. if l > q[0]:
                ind = q.pop(0)
                check if arr[ind] in map and its val == ind: so pop arr[ind] from map
                bcoz it is not present in our current window 
                
             e. if r+1 > k: res.append(len(m.keys())) l += 1
             r += 1
             return res
             
     IB: https://www.interviewbit.com/problems/distinct-numbers-in-window/       
"""
class Solution:
    def dNums(self, arr, k):

            res = []
            dq = []
            s = {}

            l, r = 0, 0
            while r < len(arr):
                dq.append(r)
                s[arr[r]] = r

                if l > dq[0]:
                    ind = dq.pop(0)
                    if arr[ind] in s and s[arr[ind]] == ind: s.pop(arr[ind])

                if r+1 >= k:
                    res.append(len(s.keys()))
                    l += 1

                r += 1
            return res
        
        
