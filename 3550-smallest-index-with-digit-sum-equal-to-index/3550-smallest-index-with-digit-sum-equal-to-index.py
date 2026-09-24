from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            # Sum the digits of nums[i]
            digit_sum = sum(int(digit) for digit in str(num))
            
            # Check if digit sum equals index
            if digit_sum == i:
                return i
                
        return -1