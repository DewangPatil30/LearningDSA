def sumDigits(n):
    
    if n < 11:
        return n
    else:
        return n%10 + sumDigits(n // 10)
    
    
print(sumDigits(1234))