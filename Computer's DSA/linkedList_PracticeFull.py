class Node:
    def __init__(self, data):
        self.data = data 
        self.ref = None
        
class LinkedList:
    def __init__(self, data=None):
        if data:
            self.head = Node(data)
            return
        self.head = None
        
    def insertL(self, data, front=False):
        if self.head is None:
            self.head = Node(data)
            return 
        
        if front:
            newNode = Node(data)
            newNode.ref = self.head
            self.head = newNode
            return
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
                
            n.ref = Node(data)
                
    def insertAfter(self, node, data):
        if self.head is None:
            print('Sorry the list is empty')
            return
        
        n = self.head
        trigger = False
        
        while n.ref is not None:
            if n.data == node:
                
                newNode = Node(data)
                newNode.ref = n.ref
                n.ref = newNode
                
                trigger = True
                return
            
            n = n.ref
                
        if trigger == False:
            print('The Node not found')
            return
        
            
    def printList(self):
        if self.head is None:
            print('The list is empty!')
            return
        
        n = self.head
        while n.ref is not None:
            print(n.data, end=' --> ')
            n = n.ref
        print()
        
    def remove(self, node):
        if self.head is None:
            print('The list is empty!')
            return
        
        if self.head.data == node:
            self.head = self.head.ref
            return
        
        n = self.head
        trigger = False
        
        while n.ref is not None:
            if n.ref.data == node:
                if n.ref.ref is not None:
                    n.ref = n.ref.ref
                else:
                    n.ref = None
                trigger = True
                return
            
            n = n.ref
        
        if trigger is False:
            print('the node not found!')
            return
    
    def pop(self, front=False):
        if self.head is None:
            print('The list is empty')
            return
        
        if self.head.ref is None:
            self.head = None
            return
        
        if front:
            self.head = self.head.ref
            return
        
        n = self.head
        while n.ref.ref is not None:
            n = n.ref
        
        n.ref = None
        return
        
    
    def index(self, node, address=False):
        if self.head is None:
            print('The list is empty!')
            return
        
        index = 0
        trigger = True
        n = self.head
        while n.ref is not None:
            if n.data == node:
                if address:
                    print(n)
                return index
            
            n = n.ref
            index += 1
        
        if trigger:
            return -1
        
        
        
def test(A):
        lst = []
        dis = []
        n = A
        while n is not None:
            lst.append(n.data)
            n = n.ref

        s = list(set(lst))
        for i in s:
            if lst.count(i) < 2:
                dis.append(i)
        print(dis)

        if dis is []:
            return None
        else:
            lst = []
            for i in dis:
                lst.append(Node(i))
            for i in range(len(lst)-1):
                lst[i].ref = lst[i+1]
    
            # return lst[0]
        
def printL(head):
    head = test(head)
    if head is None:
        print(None)
        return
    
    while head is not None:
        print(head.data, ' --> ', end='')
        head = head.ref
        
    
    
    
    
obj = LinkedList()
lst = list(map(int, input().split()))
for i in lst:
    obj.insertL(i)
    
printL(obj.head)

