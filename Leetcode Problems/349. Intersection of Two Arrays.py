'''349. Intersection of Two Arrays

https://leetcode.com/problems/intersection-of-two-arrays/description/
'''

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        intersect = set(nums1).intersection(nums2)
        for i in intersect:
            result.append(i)
        return result