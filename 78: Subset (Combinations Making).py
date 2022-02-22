from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def comb(arr, n):
            if n == 0:
                return [[]]
            temp = []
            
            for i in range(len(arr)):
                m = arr[i]
                rem = arr[i+1:]
                
                for j in comb(rem, n-1):
                    temp.append([m]+j)
            return temp
        
        res = []
        for i in range(len(nums)+1):
            res.extend(comb(nums, i))
            
        return res

#         res = []
#         for i in range(len(nums)+1):
#             res.extend(combinations(nums, i))
            
#         return res
