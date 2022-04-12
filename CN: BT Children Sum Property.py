"""
    Children Sum property: each node's value must be equal to left.val + right.val
                           So its pretty easy to make tree a children sum tree
                      But in this ques we are not allowed to decrement the cur value 
                      we can only increment the val of cur node
                      
    Intution: for each node check if left + right >= curr if yes than cur = left + right
              If not than: left = curr.val and right = cur.val. Repeat this till leaf node 
              After that return left and right and update cur.val = left + right
              
    Approach:  TC: O(N)      SC:O(1)
            a. child = 0
               if root.left: child += root.left.data
               same for right
            
            b. if child >= root.data: root.data = child
               else: 
                    if root.left: root.left.data = root.data        #ie, current node data
                    if root.right: same as above
             
             c. call function(root.left)
                     function(root.right)
             d. total = 0, do same sum as done for child
             e. if root.left or root.right: root.data = totoal   #only assign total to non leaf
             
      
      CN: https://www.codingninjas.com/codestudio/problems/childrensumproperty_790723?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1
      YT: https://www.youtube.com/watch?v=fnmisPM6cVo
"""
def changeTree(root): 
    
	if not root: return

	child = 0
	if root.left: child += root.left.data
	if root.right: child += root.right.data
	
	if child >= root.data: root.data = child
	else:
		if root.left: root.left.data = root.data
		if root.right: root.right.data = root.data
		
	changeTree(root.left)
	changeTree(root.right)
	
	tot = 0
	if root.left: tot += root.left.data
	if root.right: tot += root.right.data
	
	if root.left or root.right: root.data = tot

        
