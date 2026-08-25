#Ques
#Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.A multiple of k is any positive integer divisible by k.

#Solution

from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        multiple = k
        
        while multiple in num_set:
            multiple += k
            
        return multiple