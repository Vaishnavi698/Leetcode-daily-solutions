from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        min_val = min(nums1)
      
        if min_val % 2 != 0:
            return True
            
       
        all_even = all(x % 2 == 0 for x in nums1)
        all_odd = all(x % 2 != 0 for x in nums1)
        
        return all_even or all_odd