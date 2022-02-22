h = [4,3,2,3,5,4,3,3,2,1]
k = 2
n = len(h)

loop = 0
count = 1

for i in range(n-2, -1, -1):
    less = 0
    if n-(i+1) < k:
        loop = n
    else:
        loop = i+1+k
        
    for j in range(i+1, loop):
        
        if loop == n:
            if h[i] > h[j]:
                less += 1
            else:
                break
            
            if less == n-(i+1):
                count+=1
                break    
   
        if h[i] > h[j]:
            less += 1
        else:
            break
        
        if less == k:
            count+=1
            break
    
            
print(count)
            
    