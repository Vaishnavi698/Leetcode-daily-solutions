from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        
        # dp[c] stores [ways_arriving_down, ways_arriving_right] for column c
        dp = [[0, 0] for _ in range(cols + 1)]
        
        # Base case for starting cell (0, 0)
        # We can enter (0,0) from top or left conceptually with 1 way each to seed the edges
        dp[1] = [1, 1]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Mirror: Swaps the incoming direction paths
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    # Empty cell: Accumulates paths from both directions
                    ways = (dp[c + 1][1] + dp[c][0]) % MOD
                    dp[c + 1] = [ways, ways]
                    
        return dp[cols][0]