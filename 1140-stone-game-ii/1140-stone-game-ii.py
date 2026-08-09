#Ques
#Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.Alice and Bob take turns, with Alice starting first.On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.The game continues until all the stones have been taken.Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

#Solution

from functools import cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
   
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

     
        @cache
        def dp(i: int, m: int) -> int:
          
            if i + 2 * m >= n:
                return suffix_sum[i]
            
       
            max_stones = 0
            for x in range(1, 2 * m + 1):
                max_stones = max(
                    max_stones, 
                    suffix_sum[i] - dp(i + x, max(m, x))
                )
            return max_stones

        return dp(0, 1)