Nclass Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        
    def add(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            
            while n.ref is not None:
                n = n.ref
                
            n.ref = new_node
            
    def print_list(self):
        
        if self.head is None:
            print('Sorry! the list is empty')
        else:
            while self.head is not None:
                print(self.head.data, '-->', end=' ')
                self.head = self.head.ref 
                
    def add_before(self, data, val):
        
        if self.head == None:
            print('Sorry! the list is empty')
            return
        
        if self.head.data == val:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return


            
        else:
            while self.head.ref is not None:
                
                if self.head.ref.data == val:
                    break
                self.head = self.head.ref

        if self.head.ref is None:
            print('Sorry! the Node not found')
            
        else:
            new_node = Node(data)
            new_node.ref = self.head.ref
            self.head.ref = new_node
            
            
    def add_after(self, data, val):
        if self.head is None:
            print('Cant add node not found')
            
        else:
            n = self.head
            while n.ref is not None:
                if n.data == val:
                    break
                n = n.ref

            if n.ref is None:
                print('node not found')
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
                
                
    def pop_start(self):
        if self.head is None:
            print('The linked list is empty')
            return
        print('Poped first node: ', self.head.data)
        self.head = self.head.ref
        
    def pop_end(self):
        if self.head is None:
            print('Cannot delete. linked list is empty')
            return
        
        if self.head.ref == None:
            print('Poped Single Element. The linked list is now empty')
            self.head = None
            return
        
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        
        print('Poped last node: ', n.ref.data)
        n.ref = None
        
       
    def pop(self, val):
        if self.head is None:
            print('The linked list is empty')
            return
        
        if self.head.data == val:
            print('poping first element: ', val)
            self.head = None
            return
        
        n = self.head
        while n.ref is not None:
            if n.ref.data == val:
                break
            
        if n.ref is None:
            print('Value not found')
            return
        print('Poping: ', val)
        n.ref = n.ref.ref






        
LL1 = LinkedList()

LL1.add(10)
LL1.add(20)

LL1.add_begin(5)
LL1.add_begin(1)

LL1.add_begin(-1)
LL1.add_begin(-5)

LL1.add_after(6, 5)
LL1.add_after(7, 6)

LL1.add_before(-2, -1)
LL1.add_before(-6, -5)

LL1.pop_start()
LL1.pop_start()
LL1.pop_end()
LL1.pop_end()
LL1.pop(-1)
LL1.pop(1)

LL1.print_list()
        
        
        
        