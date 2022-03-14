"""
APPROACH :- Use Map

    The idea is to use maps. We initially insert all elements of the first row in an map. For every other element in remaining rows, 
    we check if it is present in the map. If it is present in the map and is not duplicated in current row, 
    we increment count of the element in map by 1, else we ignore the element. 
    If the currently traversed row is the last row, we print the element if it has appeared m-1 times before. 
    Below is the implementation of the idea:

GFG: https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/
"""

def printCommonElements(mat):
 
    mp = dict()
 
    # initialize 1st row elements
    # with value 1
    for j in range(N):
        mp[mat[0][j]] = 1
 
    # traverse the matrix
    for i in range(1, M):
        for j in range(N):
             
            # If element is present in the
            # map and is not duplicated in
            # current row.
            if (mat[i][j] in mp.keys() and
                             mp[mat[i][j]] == i):
                                  
            # we increment count of the
            # element in map by 1
                mp[mat[i][j]] = i + 1
 
                # If this is last row
                if i == M - 1:
                    print(mat[i][j], end = " ")
        
        
        
