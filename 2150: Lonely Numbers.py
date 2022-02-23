class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        m = dict()
        setn = set()
        
        for i in nums:
            if i not in setn:
                setn.add(i)
                m[i] = 1
            else:
                if i in m:
                    m.pop(i)
                    
        nums = set(nums)
        setn = set(m.keys())
        for i in setn:
            if i+1 in nums or i-1 in nums:
                if i in m:
                    m.pop(i)
                    
        return list(m.keys())
