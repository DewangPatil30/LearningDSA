class bst:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
    def insert(self, data):
        if self.data == None:
            self.data = data
            return 
        
        if self.data == data: 
            return
        
        if self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = bst(data)
                return
        elif self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = bst(data)
                return
            
    def preorder(self):
        
        print(self.data, end=' ')
        
        if self.left:
            self.left.preorder()
        
        if self.right:
            self.right.preorder()
        
            
    def inorder(self):
        
        if self.left:
            self.left.preorder()
        
        print(self.data, end=' ')
        
        if self.right:
            self.right.preorder()
        
    def postorder(self):
        
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print(self.data, end=' ')            
        
    def delete(self, data):
        
        if self.data == None:
            print('The tree is empty')
            return
        
        if self.data > data:
            if self.left:
                self. left = self.left.delete(data)
            else:
                print('The node not found')
                
        elif self.data < data:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print('The node not found')
        
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            else:
                node = self.right
                while node.left:
                    node = node.left
                    
                self.data = node.data
                self.right = self.right.delete(node.data)
                
            return self
        
        
        
        
        
        
        
            
node = bst()
n = [5,3,6,3,7]
for i in n:
    node.insert(i)
    
# node.preorder()
# print()
node.inorder()
print()
# node.postorder()
# print()

node.delete(5)
node.inorder()
    

                
            