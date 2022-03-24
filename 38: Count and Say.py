"""
Approach :
    Take n-1's string and just count frequency of the current term till the next term is not different, 
    If next term is different than update result string S with freq + curr and update curr = returned str[i] and freq = 1

LeetCode 38: https://leetcode.com/problems/count-and-say/ 
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        def cas(n):
            
            if n == 1: return '1'
            elif n == 2: return '11'

            ret = cas(n-1)
            curr = ret[0]
            freq = 1
            s = ''

            for i in range(1, len(ret)):
                if ret[i] == curr:
                    freq += 1
                else:
                    s += str(freq) + curr
                    curr = ret[i]
                    freq = 1

            s += str(freq) + curr
            return s
            
        return cas(n)        
      
      
