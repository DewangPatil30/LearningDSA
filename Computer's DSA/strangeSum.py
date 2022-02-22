from functools import reduce
from math import pow
import time

start_time = time.time()

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    res = 0
    
    for i in range(1, n+1):
        count = 0
        l = list(set(reduce(list.__add__, ([j, n//j] for j in range(1, int(i**0.5) + 1) if i % j == 0))))
        count = len(l)
        res += (int(pow(i, m))) * count
        
    print(res % 1000000007)


print('execution time:', time.time() - start_time)    