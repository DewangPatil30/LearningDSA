"""
Approaches:

    1. Brute Force: add ele than travase till 0'th index if any in b/w > st[-1] break and return the count of travarsal
        TC: O(N*N) SC: O(N)
        
    2. Using Stack: TC: O(N) SC: O(N)
        
        self.args or self.len += 1
        a. If stack is empty or stack.top.price > curPrice: stack.push([self.args-1, curPrice])
        b. else: pop from stack till st and st[-1].price <= curPriceL
            store poped index and price 
          After all smaller is taken out, stack.append([ind, curPrice])
          
        return self.args - ind
     
     LeetCode 901: https://leetcode.com/problems/online-stock-span/
"""

class StockSpanner:

    def __init__(self):
        self.st = []
        self.args = 0

    def next(self, price: int) -> int:
        self.args += 1
        if not self.st or self.st[-1][1] > price:
            self.st.append([self.args-1, price])
            return 1
        else:
            while self.st and self.st[-1][1] <= price:
                ind, val = self.st.pop()
            self.st.append([ind, price])
            return self.args - ind 
            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
