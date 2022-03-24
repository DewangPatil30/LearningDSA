"""
Approach: Gready 2 ptr technique
    If the heaviest person can share a boat with the lightest person, then do so. Otherwise, the heaviest person can't pair with anyone, so they get their own boat.
    The reason this works is because if the lightest person can pair with anyone, they might as well pair with the heaviest person.
    
     1. Maintain 2 pointers lo and hi set to 0 and n-1 respectively.
     2. Sort the array people.
     3. Now traverse till lo <= hi.
     4. If people[lo] + people[hi] <= target. That means they can form a pair and can sit in the same boat.
     5. If not then the people[hi] that is the person with the higher weight is the problem and must be given his own boat as we observed above.
  
LeetCode 881: https://leetcode.com/problems/boats-to-save-people/
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        boats = 0
        people = list(reversed(sorted(people)))
        l, r = 0, len(people)-1
        while l <= r:
            if people[l] + people[r] <= limit:
                r -= 1
            l += 1
            boats += 1
            
        return boats
                
        
