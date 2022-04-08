"""
Approach: 
        
        1. Recursion: TC:O(N*N) SC:O(N) Recursive:
            
            a. till there is ele in stack..... 
                x = st.pop()
                reverse(st)
                sort(st, x)
                
            b. in sort, if not stack or staxk[-1] < x:
                stack push(x) else: a = stack.pop()
                sort(st,x), stack.push(a)
                
            Return stack
            
         CN: https://www.codingninjas.com/codestudio/problems/sort-a-stack_985275?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1
         YT: https://www.youtube.com/watch?v=XNAv8NrAwng
"""

class Stack:
	def __init__(self, stack):
		self.st = stack
	
	def getStack(self):
		return self.st
	
	def sort(self, x):
		if not self.st or self.st[-1] < x:
			self.st.append(x)
		else:
			a = self.st.pop()
			self.sort(x)
			self.st.append(a)
			
	
	def reverse(self):
		if self.st:
			x = self.st.pop()
			self.reverse()
			self.sort(x)
	

def sortStack(stack):
	stack = Stack(stack)
	stack.reverse()
	return stack.getStack()
