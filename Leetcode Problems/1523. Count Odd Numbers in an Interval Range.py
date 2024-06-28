'''1523. Count Odd Numbers in an Interval Range

https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 != 0 and high % 2 != 0:
            return ((high-low+1) - (high-low+1)//2)

        if low % 2 == 0 and high % 2 == 0:
            return ((high-low+1) - (high-low+2)//2)

        if low % 2 == 0 and high % 2 != 0:
            return ((high-low+1) - (high-low+1)//2)
        
        if low % 2 != 0 and high % 2 == 0:
            return ((high-low+1) - (high-low+1)//2)