"""
Approach:
    
    1. Bit Operations: TC: O(2^N) 
        
        a. loop from 0 to (2^n)-1
        b. take empty str sub and run another loop 0 to n-1
        c. if (i & 1<<j) sub += s[j]
        d. if sub than append in res
        
        NOTES: 1 << n equivalent to 2^n,,,, a leftshift b means shift ath bits to the b left position same with right
                i & 1<<j means its the set if result is non 0 than its set
    GFG: https://practice.geeksforgeeks.org/problems/power-set4302/1#
    YT: https://www.youtube.com/watch?v=b7AYbpM5YrE
"""
class Solution:
	def AllPossibleStrings(self, s):
		
		n = len(s)
		res = []
		for i in range(1<<n):
		    sub = ""
		    for j in range(n):
		        if (i & 1<<j): sub += s[j]
		  
		    if sub: res.append(sub)
		    
		return sorted(res)
    
    
