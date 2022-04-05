"""
Approach:
      Intution: Take the item whose PROFIT PER UNIT (ie, Profit[i]/Weight[i]) is maximum and add it to Knapsack 
                if its weight + current weight in knapsack <= Limit Weight. Else take remaining weight * Profit PU in ans
        
      Greedy:
        1. Make an array of [(Profit/weight), index] for each item
        2. Sort new array in reverse order based on profit per unit weight
        3. In loop of new array, If current Weight + weight of whole item <= Limit Weight 
            than add whole profit in ans and whole weight in current weight 
        4. Else ans += (Limit weight - current weight) * profit per unit weight, break
        Return ans
        
      GFG: https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1#
      YT: 
        1. Abdul Bari Explaination: https://www.youtube.com/watch?v=oTTzNMHM05I&t=599s
        2. Code Exp: https://www.youtube.com/watch?v=IIU646w5rZI  
"""

class Solution:
    def fractionalknapsack(self, W,Items,n):
        
        ratios = []
        for i in range(len(Items)):
            x = Items[i].value / Items[i].weight
            ratios.append([x, i])
        
        ratios = sorted(ratios, key=lambda x: x[0], reverse=True)

        currW = 0
        res = 0
        for i in range(len(ratios)):
            if (currW + Items[ratios[i][1]].weight) <= W:
                currW += Items[ratios[i][1]].weight
                res += Items[ratios[i][1]].value
                
            else:
                res += (W - currW) * ratios[i][0]
                currW += (W - currW)
                break
                
        return res
