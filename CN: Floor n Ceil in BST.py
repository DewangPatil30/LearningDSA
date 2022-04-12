"""
   1. Floor: Greatest value in BST which is smaller than or equal to ‘X’.
        TC: O(N)  SC: O(1)
        
        a. rt = -1, cur = root
        b while cur:    
            if cur.data <= x:
                rt = cur.data
                cur = cur.right
            else: cur = cur.left
            
   2. Ceil: Smallest value in BST that is greater than or equal to a given number. ie, opposit of floor
        TC: O(N)       SC: O(1)
        
        a. if cur.data >= x:
                rt = cur.data
                cur = cur.left
           else: cur = cur.right
                     
   CN Floor: https://www.codingninjas.com/codestudio/problems/floor-from-bst_920457?source=youtube&amp;campaign=Striver_Tree_Videos&amp;utm_source=youtube&amp;utm_medium=affiliate&amp;utm_campaign=Striver_Tree_Videos&leftPanelTab=0
      Ceil: https://www.codingninjas.com/codestudio/problems/ceil-from-bst_920464?source=youtube&amp;campaign=Striver_Tree_Videos&amp;utm_source=youtube&amp;utm_medium=affiliate&amp;utm_campaign=Striver_Tree_Videos&leftPanelTab=0
   YT: https://www.youtube.com/watch?v=xm_W1ub-K-w
"""

######## FLOOR ########
def floorInBST(root, x):
	rt = None
	cur = root
	while cur:
        if cur.data <= x:
			rt = cur.data
			cur = cur.right
		else:
			cur = cur.left
			
	return rt

######## CEIL ##########
def findCeil(root, x):
    # Write your code here.
	rt = -1
	cur = root
	while cur:
		if cur.data >= x:
			rt = cur.data
			cur = cur.left
		else:
			cur = cur.right
			
	return rt


