class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
        
class DoublyLL:
    def __init__(self):
        self.head = None
        
    def add_begin(self, data):
        
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return 
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.head.next.prev = self.head
        
        
    def add(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        if self.head.next is None:
            self.head.next = new_node
            new_node.prev = self.head
            return
        
        n = self.head
        while n.next is not None:
            n = n.next
            
        n.next = new_node
        new_node.prev = n
        
  
    def printL(self, reverse=False):
        if self.head is None:
            print('Linked List is empty')
            return 
        
        if reverse is True:
            n = self.head
            while n.next is not None:
                n = n.next
                
            while n is not None:
                print(n.data, '-->', end=' ')
                n = n.prev
            return
            
        
        n = self.head
        while n is not None:
            print(n.data, '-->', end=' ')
            n = n.next    
        print()
        
    
    def insert_after(self, val, data):
        if self.head is None:
            print('Cannnot complete, The list is empty')
            return
        
        if self.head.data == val:
            new_node = Node(data)
            self.head.next = new_node
            new_node.perv = self.head
            
            return
        
        n = self.head
        while n.next is not None:
            if n.data == val:
                break
            n = n.next

        if n.next is None:
            print('the node with data ', val, ' not found!')
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
            new_node.prev = n
            new_node.next.prev = new_node 
    
    def insert_before(self, val, data):
        if self.head is None:
            print('Cannnot complete, The list is empty')
            return
        
        if self.head.data == val:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            new_node.next.prev = new_node            
            
            return
        
        n = self.head
        while n.next is not None:
            if n.next.data == val:
                break
            n = n.next
        
        if n.next is None:
            print('Node with data ', val, ' not found!')
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node            
            new_node.prev = n
            new_node.next.prev = new_node
            
            
            
    def pop(self, side=None):
        if self.head is None:
            print('Cannot complete, the list is empty')
            return
        if self.head.next is None:
                print('poping a node: ', self.head.data)
                self.head = None
                return
        if side == 'front':
            print('poping starting node: ', self.head.data)
            self.head.next.prev = None
            self.head = self.head.next 
            return
        
        
        n = self.head
        while n.next is not None:
            if n.next.next is None:
                break
            n = n.next
                
        print('poping rear: ', n.data) 
        n.next.prev = None
        n.next = None
            
            
        
        
        
        
    def pop_node(self, val):
        if self.head is None:
            print('List is already empty')
            return
            
        if self.head.data == val:
            print('deleted node: ', val)
            
            if self.head.next is None:
                self.head = None
                return
            else:
                self.head.next.prev = None
                self.head = self.head.next
                
                return
        n = self.head 
        while n.next is not None:
            if n.next.data == val:
                break
            n = n.next
                
        if n.next is None:
            print('Sorry, the node ', val, ' not found')
        else:
            n.next.prev = None
            n.next.next.prev = n
            n.next = n.next.next
             
        
d = DoublyLL()
for i in range(5):
    d.add(int(input('Enter a node data: ')))
    
d.add_begin(10)
d.pop(side='front')
d.insert_before(30, 20)
d.insert_before(20, 10)
            
d.printL()
d.printL(reverse=True)