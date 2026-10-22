from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        
        def check(step: int) -> bool:
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n
                if nums[prev] > nums[curr]:
                    return False
            return True
            
        ans = math.inf
        
        # Check ascending order path (step = 1)
        if check(1):
            ans = min(ans, zero)             # Direct left rotations
            ans = min(ans, n - zero + 2)     # Reverse + rotate + reverse pattern
            
        # Check descending order path (step = -1)
        if check(-1):
            ans = min(ans, zero + 2)         # Rotate + reverse pattern
            ans = min(ans, n - zero)         # Reverse + rotate pattern
            
        return ans if ans != math.inf else -1