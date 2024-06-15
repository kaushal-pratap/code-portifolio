'''1122 Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

'''

class Solution:
    def relativeSortArray(self, arr1, arr2):
        new_array = []
        k = 0
        for i in range(len(arr2)):
         
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    new_array.append(arr1[j])
                    arr1[j] = 6969709090123445675454

        for k in sorted(arr1):
            if k != 6969709090123445675454:
                new_array.append(k)
        return new_array
    
