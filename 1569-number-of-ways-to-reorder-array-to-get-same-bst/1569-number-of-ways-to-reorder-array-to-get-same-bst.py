from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Step 1: Precompute combinations using Pascal's Triangle
        comb = [[0] * n for _ in range(n)]
        for i in range(n):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
                
        # Step 2: Recursive helper function
        def dfs(arr: List[int]) -> int:
            if len(arr) <= 2:
                return 1
                
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            left_ways = dfs(left)
            right_ways = dfs(right)
            
            # Number of ways to interleave left and right subarrays
            interleave_ways = comb[len(left) + len(right)][len(left)]
            
            # Combine results modulo 10^9 + 7
            return (interleave_ways * left_ways % MOD) * right_ways % MOD
            
        # Subtract 1 to exclude the original array order
        return (dfs(nums) - 1 + MOD) % MOD