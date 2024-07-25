def countingSort(array):
    max_val = 0 #Find the maximum element in the array to find the 'k' range
    for j in array:
        if j > max_val:
            max_val = j
    
    count = [0]*(max_val+1)
    output = [0]*(len(array))
    
    for num in array:
        count[num] += 1
        
    for i in range(1,len(count)):
        count[i] += count[i-1]    
    
    print(count)

array = [2,1,2,3,1,2,4]
countingSort(array)