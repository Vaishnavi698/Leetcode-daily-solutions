#Ques
#You are given a 0-indexed array of integers nums.A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.


#Solution

class Solution:
    def missingInteger(self, nums: list[int]) -> int:
      
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
                
      
        num_set = set(nums)
        ans = prefix_sum
        while ans in num_set:
            ans += 1
            
        return ans