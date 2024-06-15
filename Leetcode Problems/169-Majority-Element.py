'''169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''

class Solution:
    
    def __init__(self):
        self.HashMap_1 = {}
        self.HashMap_2 = {}
        
    def majorityElement(self, nums: list[int]):
        for i in nums:
            if i in self.HashMap_1:
                self.HashMap_1[i] += 1
            else:
                self.HashMap_1[i] = 1
        
        for i in self.HashMap_1:
            self.HashMap_2[self.HashMap_1[i]] = i
        
        return self.HashMap_2[max(self.HashMap_2)]

