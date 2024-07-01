class MergeSort():
    def algorithm(self,arr1,arr2):
        result = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            result.append(arr1[i])
            i += 1
        while j < len(arr2):
            result.append(arr2[j])
            j += 1
        print(result)
        
M = MergeSort()
arr1 = [1,2,4,6,8,9,10,34]
arr2 = [3,7,11,21,25,31,55,61,78,91]
M.algorithm(arr1,arr2)