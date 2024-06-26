'''229. Majority Element II

https://leetcode.com/problems/majority-element-ii/description/
'''
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        HashMap = {}
        array = []
        for i in nums:
            try:
                HashMap[i] = HashMap[i] + 1
            except:
                HashMap[i] = 1

        for j in HashMap:
            if HashMap[j] > len(nums)/3:
                array.append(j)

        return array