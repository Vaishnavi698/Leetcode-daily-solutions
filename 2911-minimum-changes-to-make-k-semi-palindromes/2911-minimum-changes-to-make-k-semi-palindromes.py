class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        inf = float('inf')
        
        # g[i][j] stores the minimum changes to make s[i-1:j] a semi-palindrome
        g = [[inf] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                m = j - i + 1
                min_changes = inf
                # Try all valid divisors d of m (1 <= d < m)
                for d in range(1, m):
                    if m % d == 0:
                        changes = 0
                        # Check each group of divisor d
                        for offset in range(d):
                            group_len = m // d
                            for c in range(group_len // 2):
                                idx1 = i - 1 + offset + c * d
                                idx2 = i - 1 + offset + (group_len - 1 - c) * d
                                if s[idx1] != s[idx2]:
                                    changes += 1
                        min_changes = min(min_changes, changes)
                g[i][j] = min_changes

        # DP table for partitioning into k substrings
        # f[i][j] = min changes to partition s[0:i] into j parts
        f = [[inf] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for h in range(j - 1, i):
                    if f[h][j - 1] != inf and g[h + 1][i] != inf:
                        f[i][j] = min(f[i][j], f[h][j - 1] + g[h + 1][i])
                        
        return f[n][k]