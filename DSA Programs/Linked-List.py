class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
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
        
        

L = LinkedList()
# L.insert_head(1)
# L.insert_head(2)
# L.insert_head(5)
# L.insert_head(8)
# L.insert_head(3)
L.insert_head(20)
print(len(L))
L.append(1)
L.append(1000)
# L.insert_head(121)
print(L)