class Solution:
    def countCommas(self, n: int) -> int:
        # For numbers up to 10^5, only numbers >= 1000 have commas, and each has exactly 1 comma.
        if n < 1000:
            return 0
        return n - 999