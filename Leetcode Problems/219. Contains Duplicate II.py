'''219. Contains Duplicate II

https://leetcode.com/problems/contains-duplicate-ii/description/
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        HashMap = {}
        for i in range(len(nums)):
            if nums[i] in HashMap:
                if abs(HashMap[nums[i]] - i) <= k:
                    return True
            HashMap[nums[i]] = i
        return False
