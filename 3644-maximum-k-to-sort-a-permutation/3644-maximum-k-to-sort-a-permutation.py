from typing import List

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        return self.maximumK(nums)

    def maximumK(self, nums: List[int]) -> int:
        ans = -1
        for i, x in enumerate(nums):
            # Only consider elements that are not in their correct sorted position
            if i != x:
                if ans == -1:
                    ans = x
                else:
                    ans &= x
                    
        return max(ans, 0)