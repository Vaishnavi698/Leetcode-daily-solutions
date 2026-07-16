#Ques
#You are given an integer array nums of length n.Construct an array prefixGcd where for each index i:Let mxi = max(nums[0], nums[1], ..., nums[i]).prefixGcd[i] = gcd(nums[i], mxi).After constructing prefixGcd:Sort prefixGcd in non-decreasing order.Form pairs by taking the smallest unpaired element and the largest unpaired element.Repeat this process until no more pairs can be formed.For each formed pair, compute the gcd of the two elements.If n is odd, the middle element in the prefixGcd array remains unpaired and should be ignored.Return an integer denoting the sum of the GCD values of all formed pairs.The term gcd(a, b) denotes the greatest common divisor of a and b.

 #Solution
 
import math
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0
        
   
        for i, x in enumerate(nums):
            mx = max(mx, x)
            prefix_gcd[i] = math.gcd(x, mx)
            
      
        prefix_gcd.sort()
        
      
        ans = 0
        left = 0
        right = n - 1
        
        while left < right:
            ans += math.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
            
        return ans