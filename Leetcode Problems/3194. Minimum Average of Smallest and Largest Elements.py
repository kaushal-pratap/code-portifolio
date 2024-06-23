'''3194. Minimum Average of Smallest and Largest Elements

https://leetcode.com/contest/weekly-contest-403/problems/minimum-average-of-smallest-and-largest-elements/description/
'''

class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        averages = []
        for i in range(int((len(nums)/2))):
            minElement = min(nums)
            maxElement = max(nums)
            averages.append((minElement + maxElement)/2)
            nums.remove(minElement)
            nums.remove(maxElement)
            print(nums)
        print(averages)
        return min(averages)