def fabbo(n):
    if n in [0, 1]:
        return n
    else:
        print(n)
        return fabbo(n-1) + fabbo(n-2)
    
print(fabbo(5))