def radixSort(array):  
    length = 0 #Find the lenght of longest key first
    for i in array:
        if len(str(i)) > length:
            length = len(str(i))
            
    for j in range(len(array)): # append the zeroes to the left of each element
        new_int = '0'*(length - len(str(array[j]))) + str(array[j])
        array[j] = (new_int)
        
    sorted_array = []
    k = length - 1
    while k >= 0:
        current = 0
        for m in range(len(array)):
            if int(array[m][k]) >= int(array[current][k]):
                current = m
                            
        sorted_array.append(array[current])  
        array[current] = '0'*length
    
        current = 0
        k -= 1
    print(array)
    print(sorted_array)
    
    
    
    


array = [1,23,5432,56,89,9,765454]
radixSort(array)

