class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n
    
    
    def insertHead(self,value):
         new_node = Node(value)
         if self.head is None:
             self.head = new_node
             self.n += 1
             return
         new_node.next = self.head
         self.head = new_node
         self.n += 1
         
           
           
L = LinkedList()
L.insertHead(1)
L.insertHead(2)
print(len(L))