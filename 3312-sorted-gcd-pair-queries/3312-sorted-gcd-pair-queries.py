#Ques
#You are given an integer array nums of length n and an integer array queries.Let gcdPairs denote an array obtained by calculating the GCD of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.For each query queries[i], you need to find the element at index queries[i] in gcdPairs.Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.The term gcd(a, b) denotes the greatest common divisor of a and b.

#Solution

import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
     
        cnt = [0] * (max_val + 1)
        for num in nums:
            cnt[num] += 1
            
      
        gcd_count = [0] * (max_val + 1)
        
   
        for g in range(max_val, 0, -1):
            
            multiples_cnt = 0
            for mult in range(g, max_val + 1, g):
                multiples_cnt += cnt[mult]
                
           
            total_pairs = multiples_cnt * (multiples_cnt - 1) // 2
        
            for mult in range(2 * g, max_val + 1, g):
                total_pairs -= gcd_count[mult]
                
            gcd_count[g] = total_pairs
            
      
        pref = [0] * (max_val + 1)
        for g in range(1, max_val + 1):
            pref[g] = pref[g - 1] + gcd_count[g]
            
     
        ans = []
        for q in queries:
            idx = bisect.bisect_right(pref, q)
            ans.append(idx)
            
        return ans