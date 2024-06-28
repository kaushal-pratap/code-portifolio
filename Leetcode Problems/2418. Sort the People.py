'''2418. Sort the People

https://leetcode.com/problems/sort-the-people/description/
'''

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        new_array = []
        result = []
        for i in range(len(names)):
            new_array.append([heights[i],names[i]])
        new_array.sort(reverse = True)
        for i in range(len(names)):
            result.append(new_array[i][1])

        return result