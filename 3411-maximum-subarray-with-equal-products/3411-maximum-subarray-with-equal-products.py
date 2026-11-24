import math


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            prod = 1
            curr_gcd = 0
            curr_lcm = 1

            for j in range(i, n):
                val = nums[j]
                prod *= val
                curr_gcd = math.gcd(curr_gcd, val)
                curr_lcm = math.lcm(curr_lcm, val)

                if prod == curr_lcm * curr_gcd:
                    max_len = max(max_len, j - i + 1)

        return max_len