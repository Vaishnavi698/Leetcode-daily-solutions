#Ques
#Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 #Solution

import math
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))