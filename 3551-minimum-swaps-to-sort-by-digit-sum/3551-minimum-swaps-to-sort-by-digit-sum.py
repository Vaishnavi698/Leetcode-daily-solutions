from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        # Pair each element with its original index
        indexed_nums = [(nums[i], i) for i in range(n)]
        
        # Sort based on digit sum, then by numerical value
        indexed_nums.sort(key=lambda x: (get_digit_sum(x[0]), x[0]))
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already visited or already in the correct position, skip
            if visited[i] or indexed_nums[i][1] == i:
                continue
                
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][1]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps