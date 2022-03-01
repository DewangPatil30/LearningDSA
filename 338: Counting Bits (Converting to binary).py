class Solution:
    def countBits(self, n: int) -> List[int]:

        # Sol 1: Raw Logic O(n2)
        
        res = []
        for i in range(n+1):
            b = ''
            while i != 0:
                b = str(i%2) + b
                i = i // 2
            res.append(b.count('1'))
            
        return res
    
    
        # Sol 2: Using int() and formatting
        
        res = []
        for i in range(n+1):
            t = "{0:b}".format(int(i))
            res.append(t.count('1'))
        return res
        
        # Sol 3: Using bin()
        
        res = []
        for i in range(n+1):
            res.append(bin(i).replace("0b", "").count('1'))
        return res
