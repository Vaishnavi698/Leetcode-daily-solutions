import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        # Combination formula C(n + k - 1, 2k) % MOD
        return math.comb(n + k - 1, 2 * k) % MOD