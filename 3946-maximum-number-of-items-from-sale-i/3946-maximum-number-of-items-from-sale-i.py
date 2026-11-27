from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        MAX_F = 1500
        freq = [0] * (MAX_F + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        # Precompute free items unlocked for each possible factor value
        free_by_factor = [0] * (MAX_F + 1)
        for f in range(1, MAX_F + 1):
            if freq[f] > 0:
                count = 0
                for multiple in range(f, MAX_F + 1, f):
                    count += freq[multiple]
                # Exclude item i itself (j != i)
                free_by_factor[f] = count - 1
                
        # 0-1 Knapsack for the first copy of each item
        dp = [-1] * (budget + 1)
        dp[0] = 0
        min_price = float('inf')
        
        for factor, price in items:
            min_price = min(min_price, price)
            gain = 1 + free_by_factor[factor]
            for c in range(budget, price - 1, -1):
                if dp[c - price] != -1:
                    dp[c] = max(dp[c], dp[c - price] + gain)
                    
        # Unbounded Knapsack for any additional copies using the cheapest item
        for c in range(min_price, budget + 1):
            if dp[c - min_price] != -1:
                dp[c] = max(dp[c], dp[c - min_price] + 1)
                
        return max(dp)
