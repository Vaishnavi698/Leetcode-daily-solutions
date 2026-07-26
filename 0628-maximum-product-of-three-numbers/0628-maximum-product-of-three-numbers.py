#Ques
#Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 #Solution

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
      
        prod1 = nums[-1] * nums[-2] * nums[-3]
        
      
        prod2 = nums[0] * nums[1] * nums[-1]
        
        return max(prod1, prod2)