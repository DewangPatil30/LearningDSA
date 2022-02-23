class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        m = dict()
        
        for i, v in enumerate(nums):
            if v in m:
                if abs(m[v] - i) <= k:
                    return True
                else:
                    m[v] = i
            else:
                m[v] = i
                    
        return False
