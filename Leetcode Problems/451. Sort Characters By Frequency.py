'''451. Sort Characters By Frequency

https://leetcode.com/problems/sort-characters-by-frequency/description/
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        HashMap = {}
        array = []
        result = ''
        for i in s:
            if i not in HashMap:
                HashMap[i] = 1
            else:
                HashMap[i] = HashMap[i] + 1
        for j in HashMap:
            array.append([HashMap[j],j])
        array = sorted(array,reverse = True)

        for k in array:
            result = result + k[1]*k[0]
        return(result)