#Ques
#You are given a 0-indexed array of distinct integers nums.There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

#Solution

from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
            
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
       
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)
        
       
        option1 = j + 1
        
      
        option2 = n - i
        
      
        option3 = (i + 1) + (n - j)
        
        return min(option1, option2, option3)