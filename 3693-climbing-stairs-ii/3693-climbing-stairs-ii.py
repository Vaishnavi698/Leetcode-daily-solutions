from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[i] represents the minimum total cost to reach step i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            # Check previous 3 possible starting steps: i-1, i-2, i-3
            for j in range(max(0, i - 3), i):
                cost = dp[j] + costs[i - 1] + (i - j) ** 2
                if cost < dp[i]:
                    dp[i] = cost
                    
        return dp[n]