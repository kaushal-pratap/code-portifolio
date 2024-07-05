class BinarySearch():
    def algorithm(self,array,target):
        n = len(array)
        left = 0
        right = n-1
        while left <= right:
            middle = (left+right)//2
            if array[middle] == target:
                print('Index : ',middle)
                return
            elif target < array[middle]:
                right = middle -1 
                
            else:
                left = middle + 1
        print('Element not found')
        return
    
B = BinarySearch()
array = [2,2]
target = 2
B.algorithm(array,target)