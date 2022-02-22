class BST:
    
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        
        
        
    def insert(self, data):
        
        if self.value == None:
            self.value = data
            return
        
        if self.value == data:
            return
        
        if self.value > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
            return 
        
        if self.value < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
            return
        
        
    def search(self, data):
        if self.value == None:
            print('tree is empty')
            return
        
        if self.value == data:
            print('Data found', data)
            return
        
        if self.value > data:
            if self.left:
                self.left.search(data)
            else:
                print('data not found', data)
        
        elif self.value < data:
            if self.right:
                self.right.search(data)
            else:
                print('data not found')
            
    def printTree(self, inorder=False, preorder=False, postorder=False):     
        if self.value == None:
            print('tree is empty')
            return
        
        if inorder:
            if self.left:
                self.left.printTree(inorder=True)
        
            print(self.value, end=' ') 
            
            if self.right:
                self.right.printTree(inorder=True)
        
        if preorder:
            print(self.value, end=' ')
            
            if self.left:
                self.left.printTree(preorder=True)
            if self.right:
                self.right.printTree(preorder=True)
        
        if postorder:
            if self.left:
                self.left.printTree(postorder=True)
            if self.right:
                self.right.printTree(postorder=True)
                
            print(self.value, end=' ')
    
    
    def preorder(self):
        if self.value == None:
            print('tree is empty')
            return
        
        print(self.value, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        
    def inorder(self):
        if self.value == None:
            print('tree is empty')
            return
        
        if self.left:
            self.left.inorder()
        
        print(self.value, end=' ') 
            
        if self.right:
            self.right.inorder()
        
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
            
        print(self.value, end=' ')
        
        
    def delete(self, data, curr):
        
        if self.value > data:
           if self.left:
               self.left = self.left.delete(data, curr)
           else:
               print('the node not found')
           return
       
        elif self.value < data:
            if self.right:
                self.right = self.right.delete(data, curr)
            else:
                print('the node not found')
            return
        
        else:
            if self.left is None:
                temp = self.right
                if data == curr:
                    self.right = temp.right
                    self.left = temp.left
                    self.value = temp.value
                    temp = None
                    return
                self = None
                return temp
            if self.right is None:
                temp = self.left
                if data == curr:
                    self.right = temp.right
                    self.left = temp.left
                    self.value = temp.value
                    temp = None
                    return
                self = None
                return temp
            
            node = self.right
            while node.left is not None:
                node = node.left
            self.value = node.value
            self.right = self.right.delete(node.value, curr)
            
        return self
    
    def minValue(self):
    
        current = self
        while current.left is not None:
            current = current.left
        print('Min Node Value: ', current.value)

    def maxValue(self):
    
        current = self
        while current.right is not None:
            current = current.right
        print('Min Node Value: ', current.value)
        
        
        
def count(root):
    if root is None:
        return 0
    else:
        return 1 + count(root.left) + count(root.right) 
        
        
        
                
root = BST()
l1 = [4]
for i in l1:
    root.insert(i)
# root.preorder()  
# print()
# root.inorder()
# print()
# root.postorder()
# print()
# root.search(6)

root.inorder()
print()

if count(root) > 1:
    root.delete(4, root.value)
else:
    print('Sorry, cannot delete root alone!')

root.inorder()
print()