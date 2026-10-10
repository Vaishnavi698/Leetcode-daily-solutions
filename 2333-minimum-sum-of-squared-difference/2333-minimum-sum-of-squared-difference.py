from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        # Step 1: Compute absolute differences and their frequencies
        max_diff = 0
        diff_count = [0] * 100001
        
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            if d > 0:
                diff_count[d] += 1
                if d > max_diff:
                    max_diff = d
                    
        # Total sum of absolute differences
        total_diffs = sum(abs(nums1[i] - nums2[i]) for i in range(n))
        if total_diffs <= total_k:
            return 0
            
        # Step 2: Greedily reduce the largest differences from top to bottom
        for d in range(max_diff, 0, -1):
            if diff_count[d] == 0:
                continue
            
            # Number of operations needed to reduce all elements currently at difference `d` down to `d - 1`
            operations_needed = diff_count[d]
            
            if total_k >= operations_needed:
                # We can reduce all elements at `d` to `d - 1`
                total_k -= operations_needed
                diff_count[d] = 0
                diff_count[d - 1] += operations_needed
            else:
                # We can only reduce a portion of elements at `d` to `d - 1`
                diff_count[d] -= total_k
                diff_count[d - 1] += total_k
                total_k = 0
                break
                
        # Step 3: Compute the final minimum sum of squared differences
        min_sum_sq = 0
        for d in range(1, len(diff_count)):
            if diff_count[d] > 0:
                min_sum_sq += diff_count[d] * (d ** 2)
                
        return min_sum_sq