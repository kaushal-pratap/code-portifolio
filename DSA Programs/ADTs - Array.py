'''Hey, This is my code for creating our own array from scratch in Python. 
This is from the topic called - Abstract Data Types'''

import ctypes 

class MyList:
    def __init__(self):
        self.n = 0
        self.size = 1
        self.A = self.make_array(self.size)
        
    def make_array(self,capacity):
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.size == self.n :
            self.resize(self.size*2)
            
        self.A[self.n] = item
        self.n += 1 
    
    def resize(self,new_capacity):
        B = self.make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
     
    def __str__(self):
        result = ''
        for i in range (self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    
    
    def __getitem__(self,index):
        if 0<= index < self.n :
            return self.A[index]
        else :
            return 'IndexError - Index out of range'
    
    def pop(self):
        if self.n == 0:
            return "IndexError: Pop empty list"
        print(self.A[self.n-1])
        self.n = self.n - 1
        
    def clear(self):
        self.n = 0
        self.size = 1
        
    def find(self,element):
        i = 1
        while i < len(self.A):
            if self.A[i-1] == element:
                return print(i-1)
                
            i += 1
        return ("Element not found")
        
    def insert(self,index,item):
        B = self.make_array(self.size+1)
        self.size += 1
        self.n += 1
        for i in range(index):
            B[i] = self.A[i]
        B[index] = item
        i = index+1
        while i < len(self.A):
            B[i] = self.A[i-1]
            i += 1
        B[len(B)-1] = self.A[len(self.A)-1]
        self.A = B
    
    def __delitem__(self,index):
        if 0 <=index > self.n-1:
            print("IndexError: Index out of range")
        
        else:
            if index == self.n-1:
                self.n = self.n - 1
            else:
                i = index
                while i < self.n-1:
                    self.A[i] = self.A[i+1]
                    i += 1
                self.n = self.n -1
                
    def remove(self,item):
        for j in range(self.n):
            if self.A[j] == item:
                self.__delitem__(j)
                
                
    def sort(self):
        self.type_state_num = None
        self.type_state_str = None
        
        for i in range(self.n):
            if type(self.A[i]) == int or type(self.A[i]) == float:
                self.type_state_num = True
            else:
                self.type_state_num = False
                break
              
        for i in range(self.n):
            if type(self.A[i]) == str :
                self.type_state_str = True
            else:
                self.type_state_str = False
                break
        
        if self.type_state_str == True:
            self.A = self.A[:self.n]
            for i in range(self.n):
                self.A[i] = self.A[i].lower()
            print(sorted(self.A))
     
        elif self.type_state_num == True:
            self.A = self.A[:self.n]
            print(sorted(self.A))

        else:
            print("ValueError: Sorting can't be performed between str and int")
            
    
    def max(self):
        self.A = self.A[:self.n]
        return max(self.A)
    
    def min(self):
        self.A = self.A[:self.n]
        return min(self.A)
    
    def sum(self):
        self.A = self.A[:self.n]
        return sum(self.A)
    
            
L = MyList()
K = MyList()
L.append('hi')
L.append("Hello World")
L.append("abc")
L.append("asWc")
L.append("D")
K.append(34)
K.append(5.6)
K.append(1.2)
K.append(90)
K.append(23)
print(K)
print(K.sum())

