def binarySearch(arr, num):
    if len(arr) < 2 and arr[0] != num:
        return -1
    
    n = len(arr) // 2
    
    if arr[n] == num:
        return n
    elif num < arr[n]:
        return binarySearch(arr[:n], num)
    else:
        return binarySearch(arr[n+1:], num)


l1 = [4,9,5,1,2,3]
l1 = sorted(l1)
ind = binarySearch(l1, 3)
print(ind)