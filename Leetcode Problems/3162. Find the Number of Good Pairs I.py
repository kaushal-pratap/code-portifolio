'''3162. Find the Number of Good Pairs I

https://leetcode.com/problems/find-the-number-of-good-pairs-i/description/
'''
class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j]*k) == 0:
                    count += 1

        return count