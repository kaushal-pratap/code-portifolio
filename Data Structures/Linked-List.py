class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
        
    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        self.n += 1
        
    def insertAtIndex(self,data,index):
        if index == 0:
            self.insertAtBegin(data)
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position += 1
            current_node = current_node.next
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print('Index not present')
        self.n += 1
            
    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node
        self.n += 1
        
    def updateNode(self,val,index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position != index):
                position += 1
                current_node = current_node.next
                
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
                
    def remove_first_node(self):
        if self.head == None:
            return
        self.head = self.head.next
        self.n -= 1
                
    def remove_last_node(self):
        if self.head == None:
            return
        current_node = self.head
        while (current_node.next != None and current_node.next.next != None):
            current_node = current_node.next
        current_node.next = None
        self.n -= 1
        
    def remove_at_index(self,index):
        if self.head == None:
            return
        
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
            self.n -= 1
        else:
            while (current_node != None and position + 1 != index):
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
            self.n -= 1
    
    def remove_node(self,data):
        current_node = self.head
        if current_node.data == data:
            self.remove_first_node()
            self.n -= 1 
            return
        while current_node != None and current_node.next.data != data:
            current_node = current_node.next
            
        if current_node == None:
            return
        current_node.next = current_node.next.next
        self.n -= 1
    
    
    
    def printLL(self):
        current_node = self.head
        while (current_node != None):
            print(current_node.data)
            current_node = current_node.next
    
            
list = LinkedList()
list.insertAtBegin('a')
list.printLL()