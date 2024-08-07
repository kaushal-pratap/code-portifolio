class Stack():
    def __init__(self):
        self.values = []
    
    def push(self,val):
        self.values.append(val)
        
        
    def is_empty(self):
        return len(self.values) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.values.pop()
        else:
            return None
        
        
        