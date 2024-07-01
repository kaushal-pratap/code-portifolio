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
array = [1,2,3,4,5,6,7,8,9,10]
target = 9
B.algorithm(array,target)