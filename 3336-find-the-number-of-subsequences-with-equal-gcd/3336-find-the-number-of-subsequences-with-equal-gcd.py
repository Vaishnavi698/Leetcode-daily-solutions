#Ques
#You are given an integer array nums.Your task is to find the number of pairs of non-empty subsequences (seq1, seq2) of nums that satisfy the following conditions:The subsequences seq1 and seq2 are disjoint, meaning no index of nums is common between them.The GCD of the elements of seq1 is equal to the GCD of the elements of seq2.Return the total number of such pairs.Since the answer may be very large, return it modulo 109 + 7.

 
#Solution

import math
from typing import List
from collections import defaultdict

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
   
        dp = {(0, 0): 1}
        
        for x in nums:
            next_dp = defaultdict(int)
            for (g1, g2), count in dp.items():
               
                next_dp[(g1, g2)] = (next_dp[(g1, g2)] + count) % MOD
                
               
                ng1 = x if g1 == 0 else math.gcd(g1, x)
                next_dp[(ng1, g2)] = (next_dp[(ng1, g2)] + count) % MOD
                
              
                ng2 = x if g2 == 0 else math.gcd(g2, x)
                next_dp[(g1, ng2)] = (next_dp[(g1, ng2)] + count) % MOD
                
            dp = next_dp
            
     
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans