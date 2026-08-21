#Ques
#You are given an integer array coins representing coins of different denominations and an integer k.You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.Return the kth smallest amount that can be made using these coins.

#Solution

import math
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        
       
        combos = []
        for r in range(1, n + 1):
            sign = 1 if r % 2 == 1 else -1
            for sub in combinations(coins, r):
                lcm_val = sub[0]
                for coin in sub[1:]:
                    lcm_val = (lcm_val * coin) // math.gcd(lcm_val, coin)
                combos.append((lcm_val, sign))
                
        def count_multiples(target: int) -> int:
            total = 0
            for lcm_val, sign in combos:
                total += sign * (target // lcm_val)
            return total

        
        left = 1
        right = min(coins) * k
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if count_multiples(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans