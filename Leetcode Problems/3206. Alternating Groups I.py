'''3206. Alternating Groups I

https://leetcode.com/contest/biweekly-contest-134/problems/alternating-groups-i/description/
'''

class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        count = 0
        if colors[1] != colors[0] and colors[1] == colors[len(colors)-1]:
             count += 1
        if colors[len(colors)-1] != colors[len(colors)-2] and colors[len(colors)-2] == colors[0]:
            count += 1
        for i in range(1,len(colors)-1):
            if colors[i-1] != colors[i] and colors[i-1] == colors[i+1]:
                count += 1

        return count
        

            
