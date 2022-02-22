def firstOcc(li, ele):
    if  len(li) < 1:
        return -1
    
    if li[0] == ele:
        return n - len(li)

    return firstOcc(li[1:], ele)    



n = int(input())
lst = list(map(int, input().split()))
ele = int(input())

print(firstOcc(lst, ele))