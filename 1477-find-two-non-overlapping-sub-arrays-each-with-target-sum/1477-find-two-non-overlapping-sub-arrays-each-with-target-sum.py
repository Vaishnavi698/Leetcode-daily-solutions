from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        
        left = 0
        current_sum = 0
        min_total_length = float('inf')
        current_min_length = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink window if current sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
            
            # If a valid sub-array with target sum is found
            if current_sum == target:
                curr_len = right - left + 1
                
                # Check if a non-overlapping valid sub-array exists before 'left'
                if left > 0 and min_len[left - 1] != float('inf'):
                    min_total_length = min(min_total_length, curr_len + min_len[left - 1])
                
                current_min_length = min(current_min_length, curr_len)
            
            # Record the minimum sub-array length found up to index 'right'
            min_len[right] = current_min_length
            
        return min_total_length if min_total_length != float('inf') else -1