n = int(input())
x = list(map(int, input().split()))

y = []
z = []
for i in range(100):
    y.append(i)
    
for i in range(100):
    z.append(-1*i)
    
    

pair = []

for k in range(len(x)):
    trigg = False
    for i in range(len(y)):
        for j in range(len(z)):
            temp = []     
            if x[k] == y[i]+z[j]:
                temp.append(y[i])
                temp.append(z[j])
                pair.append(temp)
                trigg = True
                break
        if trigg:
            break
print(pair)