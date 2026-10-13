from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Step 1: Square every element and sort them
        squares = sorted([x * x for x in nums])
        
        n = len(squares)
        m = n // 2  # Number of elements to subtract
        
        # Step 2: Subtract the smallest squares and add the rest
        ans = 0
        for i in range(m):
            ans -= squares[i]
        for i in range(m, n):
            ans += squares[i]
            
        return ans