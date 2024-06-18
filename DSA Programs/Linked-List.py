class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList(Node):
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n
    
    
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1
    
    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result = result + str(current.data) + ' -> '
            current = current.next
        return result[:-4]
            
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        self.n += 1
        
    def insert(self,value,index):
        new_node = Node(value)
        current = self.head
        if self.head == None:
            self.head = new_node
            self.n += 1
            return

        count = 0
        while count < index - 1:
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node
        self.n += 1
    
    def clear(self):
        self.head = None
        self.n = 0
        
    def delete_head(self):
        if self.head == None:
            return 'Error : Linked List empty'
        self.head = self.head.next
        self.n = self.n - 1
        
    def pop(self):
        if self.head == None:
            return 'Error : Empty Linked List'
        
        current = self.head
        if current.next == None:
            self.delete_head()
            return
        
        while current.next.next!= None:
            current = current.next
        current.next = None   
        self.n = self.n - 1     
                
                
    def delete(self,value):
        current = self.head
        try :
            
            if current == None:
                return 'Emptu linked list'
            
            if current.data == value:
                self.delete_head()
                return
            while current.next.data != value:
                current = current.next
            if current.next.data == value:
                current.next = current.next.next
                self.n -= 1
                return
        except:
             print('ELemet Not Found')
        
    
    def find(self,value):
        index = 0
        current = self.head
        while current != None:
            if current.data == value:
                print(index)
                return
            index += 1
            current = current.next
        print('Element Not found')
        return
    
    def __getitem__(self,index):
        current = self.head 
        pos = 0
        while current != None:
            if pos == index:
                print(current.data)
                return
            pos += 1
            current = current.next
        return 'Index out of range'




L = LinkedList()
# L.insert_head(1)
# L.insert_head(2)
# L.insert_head(5)
# L.insert_head(8)
# L.insert_head(3)
L.insert_head(20)
L.append(1)
L.append(1000)
L.insert('hi',1)
# L.insert_head(121)
L.delete(1)
L.find(20)
print(L)
print(len(L))
print(L[0])