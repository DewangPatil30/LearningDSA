"""
Approaches:
        
        1. Using Dict and Sort using Lambda: TC: NlogN  SC: N
            instead of freq[string] += 1 we will use -= 1 so that is can be sorted in
            descending in freq and ascendin in lexcalogical
            
        2. Dict and Heap Using Comparator (IMPRESSIVE): TC SC Same as above
        
LeetCode 692: https://leetcode.com/problems/top-k-frequent-words/
"""
############ MY SOL> ############
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = defaultdict(int)
        for s in words:  freq[s] -= 1     
        res = []
        
        for s, f in sorted(freq.items(), key=lambda x: (x[1], x[0])):
            k -= 1
            res.append(s)
            if not k: return res
            
            
################## USING COMPARATOR ###############

# https://leetcode.com/problems/top-k-frequent-words/discuss/538903/Python-O(N-log(k))-code-using-heap-to-sort-by-multiple-attributes

from heapq import heappush, heappop, heappushpop

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapper = defaultdict(int)
        for word in words:
            mapper[word] += 1
        
        h = list()
        for word, freq in mapper.items():
            node = Node(word, freq)
            if len(h) == k:
                heappushpop(h, node)
            else:
                heappush(h, node)
                
        result = list()
        while h:
            result.append(heappop(h).word)
        return result[::-1]
    
    
