class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n
    
    def insert_at_head(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        new_node.next = self.head
        self.head = new_node
        self.n += 1
        
    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result += str(current.data) + ' -> '
            current = current.next
            
        return result[:-4]
    
    
    def append(self,value):
        if self.head == None:
            return self.insert_at_head(value)
        new_node = Node(value)
        current = self.head 
        while current.next != None:
            current = current.next
        current.next = new_node
        self.n += 1
        
        
    def insert(self,value, index):
        new_node = Node(value)
        if self.head == None:
            return self.insert_at_head(value)
        current = self.head
        position = 0
        while current != None and position != index:
            current = current.next
            position += 1
        if current != None:
            new_node.next = current.next
            current.next = new_node
            self.n += 1
        else:
            print("Index not found")
            r
        self.head = None
        self.n = 0
        
    def delete_head(self):
        if self.head == None:
            print("Linked List already empty")
            return
        
        self.head = self.head.next
        self.n -= 1
        
    def pop(self):
        if self.head == None:
            return 'Linked List is empty'
        current = self.head
        if current.next == None:
            self.delete_head()
            return
        while current.next.next != None:
            current = current.next
        current.next = None
        self.n -= 1
        
    def delete(self,value):
        current = self.head
        if self.head == None:
            return 'Linked List is empty'
        if self.head.data == value:
            return self.delete_head()
        while current.next.next != None:
            if current.next.data == value:
                current.next = current.next.next
                self.n -= 1
                return
            current = current.next
        while current.next != None:
            current = current.next
        if current.data == value:
            return self.pop()
        return 'Value not found'
    
    
    def find(self,value):
        index = 0
        current = self.head
        while current != None:
            if current.data == value:
                return index
            index += 1
            current = current.next
        return 'Element not found'
    

    
    
    
L = LinkedList()
L.append(9)
L.insert_at_head(10)
L.insert(2,0)
L.append(98)
L.delete(98)
L.find(9)
print(L)
print(len(L))
        
    