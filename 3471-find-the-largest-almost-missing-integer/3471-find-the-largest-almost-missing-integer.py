#Ques
#You are given an integer array nums and an integer k.An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.Return the largest almost missing integer from nums. If no such integer exists, return -1.A subarray is a contiguous sequence of elements within an array.

#Solution

from collections import defaultdict

class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        subarray_count = defaultdict(int)
        
       
        for i in range(n - k + 1):
            unique_in_window = set(nums[i : i + k])
            for num in unique_in_window:
                subarray_count[num] += 1
                
        ans = -1
        for num, count in subarray_count.items():
            if count == 1:
                ans = max(ans, num)
                
        return ans