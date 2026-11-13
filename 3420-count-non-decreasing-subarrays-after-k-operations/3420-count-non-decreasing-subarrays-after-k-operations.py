from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 0
        current_cost = 0
        r = n - 1
        
        # Monotonic decreasing deque storing indices of running maximums
        dq = deque()
        
        for l in range(n - 1, -1, -1):
            # Pop elements from front that are <= nums[l] and update cost
            while dq and nums[dq[0]] <= nums[l]:
                idx = dq.popleft()
                next_idx = dq[0] if dq else r + 1
                block_len = next_idx - idx
                current_cost += block_len * (nums[l] - nums[idx])
                
            dq.appendleft(l)
            
            # Shrink window from the right if operations exceed k
            while current_cost > k:
                # The rightmost element r is governed by dq[-1]
                current_cost -= nums[dq[-1]] - nums[r]
                if dq[-1] == r:
                    dq.pop()
                r -= 1
                
            # All subarrays starting at l and ending in [l, r] are valid
            ans += (r - l + 1)
            
        return ans