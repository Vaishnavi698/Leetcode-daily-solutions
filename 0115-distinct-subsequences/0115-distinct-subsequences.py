class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        # dp[j] stores the number of subsequences of s matching t[:j]
        dp = [0] * (m + 1)
        dp[0] = 1  # Base case: empty string t can always be matched once
        
        for char in s:
            # Iterate backwards to avoid using updated values from the same step
            for j in range(m - 1, -1, -1):
                if char == t[j]:
                    dp[j + 1] += dp[j]
                    
        return dp[m]