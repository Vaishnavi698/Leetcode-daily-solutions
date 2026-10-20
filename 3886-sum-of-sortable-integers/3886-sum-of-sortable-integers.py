from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        return self.sumOfSortableIntegers(nums)

    def sumOfSortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Precompute prefix maximums
        pref_max = [0] * (n + 1)
        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])
            
        # 2. Precompute suffix minimums
        suff_min = [float('inf')] * (n + 1)
        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])
            
        # 3. Precompute prefix count of adjacent descents (nums[i-1] > nums[i])
        pref_drop = [0] * n
        for i in range(1, n):
            pref_drop[i] = pref_drop[i - 1] + (1 if nums[i - 1] > nums[i] else 0)
            
        def check_block(l: int, r: int) -> bool:
            descents = pref_drop[r] - pref_drop[l] if r > l else 0
            if nums[r] > nums[l]:
                descents += 1
            return descents <= 1

        total_sum = 0
        
        # 4. Check every divisor k of n
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            possible = True
            for i in range(0, n, k):
                l, r = i, i + k - 1
                if not check_block(l, r):
                    possible = False
                    break
                if i + k < n and pref_max[i + k] > suff_min[i + k]:
                    possible = False
                    break
                    
            if possible:
                total_sum += k
                
        return total_sum