#Ques
#You are given an integer array nums.Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.

#Solution

class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        has_non_zero = False
        
        for x in nums:
            total_xor ^= x
            if x != 0:
                has_non_zero = True
                
        if total_xor != 0:
            return len(nums)
        elif has_non_zero:
            return len(nums) - 1
        else:
            return 0