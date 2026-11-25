class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        base = 10**9 + 7
        mod = (1 << 61) - 1

        def has_unique_of_len(length: int) -> bool:
            if length > n:
                return False
            power = pow(base, length - 1, mod)
            h = 0
            for i in range(length):
                h = (h * base + nums[i]) % mod

            counts = {h: 1}
            for i in range(length, n):
                out_val = (nums[i - length] * power) % mod
                h = (h - out_val + mod) % mod
                h = (h * base + nums[i]) % mod
                counts[h] = counts.get(h, 0) + 1

            return any(freq == 1 for freq in counts.values())

        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_len(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
