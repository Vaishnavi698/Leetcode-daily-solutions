#Ques:-
#You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri]. For each queries[i], extract the substring s[li..ri]. Then, perform the following: Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.  Let sum be the sum of digits in x. The answer is x * sum. Return an array of integers answer where answer[i] is the answer to the ith query. Since the answers may be very large, return them modulo 109 + 7.

#Solution:-

import bisect
from typing import List

class Solution:
    
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
      
        nz_indices = []      
        nz_digits = []      
        nz_prefix_val = []  
        
        digit_pref = [0] * (len(s) + 1)
        for i, char in enumerate(s):
            val = int(char)
            digit_pref[i + 1] = digit_pref[i] + val
            
            if val != 0:
                nz_indices.append(i)
                nz_digits.append(val)
               
                if not nz_prefix_val:
                    nz_prefix_val.append(val % MOD)
                else:
                    nz_prefix_val.append((nz_prefix_val[-1] * 10 + val) % MOD)
                    
     
        pow10 = [1] * (len(nz_digits) + 1)
        for i in range(1, len(nz_digits) + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        ans = []
        
        for l, r in queries:
         
            total_sum = digit_pref[r + 1] - digit_pref[l]
            
            if total_sum == 0:
                ans.append(0)
                continue
                
          
            left_idx = bisect.bisect_left(nz_indices, l)
            right_idx = bisect.bisect_right(nz_indices, r) - 1
            
            if left_idx > right_idx:
                ans.append(0)
                continue
                
           
            num_digits = right_idx - left_idx + 1
            
            high_val = nz_prefix_val[right_idx]
            low_val = nz_prefix_val[left_idx - 1] if left_idx > 0 else 0
            
           
            x = (high_val - (low_val * pow10[num_digits]) % MOD) % MOD
            
           
            ans.append((x * total_sum) % MOD)
            
        return ans