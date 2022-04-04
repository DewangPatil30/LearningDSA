"""
Approach:
      
      For example, we divide(5000, 14):

        1. After the first inner loop: the_sum = 3584 which is 14 multiplied 256 times.
        2. We can't multiply any more — because after 256 is coming 256 + 256 = 512 and 14 * 512 = 7168 which is larger than our dividend, so we exit the inner loop,
        3. Reducing dividend: dividend = 5000 - 3584 = 1416
        4. And moving to another cycle of outer loop
        5. After the second inner loop: the_sum = 896 which is 14 multiplied 64 times.
        6. Third: the_sum = 448 which is 14 multiplied 32 times. And so on
        7. Finally we have: quotient = 256 + 64 + 32 + 4 + 1 = 357
        
    LeetCode 29: https://leetcode.com/problems/divide-two-integers/
"""

class Solution:
    def divide(self, divi: int, divs: int) -> int:
        
        nege = (divi < 0) != (divs < 0)
        divi = abs(divi)
        divs = abs(divs)
            
        res = 0
        s = divs
        while s <= divi:
            curr = 1
            while s + s <= divi:
                s += s
                curr += curr
            divi -= s
            s = divs
            res += curr
            
        return min(max(-2147483648, -res if nege else res), 2147483647)
      
      
