# l1 = list(map(int, input().split(',')))
# k = int(input())

# l1 = sorted(l1)
# count = 1
# final = []

# for i in range(len(l1)-1):
#     if l1[i] == l1[i+1]:
#         count += 1
#     else:
#         count = 1
    
#     if count > len(l1) // k:
#         if l1[i] not in final:
#             final.append(l1[i])
            
# print(*final)
        

l1 = list(map(int, input().split(',')))
maxSoFar = 0
maxEnd = 0

for i in l1:
    maxEnd += i
    
    if maxEnd < 0:
        maxEnd = 0
    elif maxEnd > maxSoFar:
        maxSoFar = maxEnd
        
print(maxSoFar)
    
    
    
    
    
    
    
    
    
    
    
    