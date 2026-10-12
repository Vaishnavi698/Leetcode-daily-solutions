from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30
        
        # Step 1: Count set bits at each position across all numbers
        for x in nums:
            for b in range(30):
                if (x >> b) & 1:
                    bit_counts[b] += 1
                    
        # Step 2: Greedily construct the k largest possible numbers
        k_nums = [0] * k
        for b in range(29, -1, -1):
            c = bit_counts[b]
            for i in range(min(c, k)):
                k_nums[i] |= (1 << b)
                
        # Step 3: Calculate the sum of squares modulo 10^9 + 7
        ans = 0
        for x in k_nums:
            ans = (ans + x * x) % MOD
            
        return ans