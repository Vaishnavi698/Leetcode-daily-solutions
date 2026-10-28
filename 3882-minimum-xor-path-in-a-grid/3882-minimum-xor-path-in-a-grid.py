from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # dp[c] will store the set of possible XOR values at column c for the current row
        dp = [set() for _ in range(cols)]
        
        # Initialize the starting cell (0, 0)
        dp[0].add(grid[0][0])
        
        # Fill the first row
        for c in range(1, cols):
            for val in dp[c - 1]:
                dp[c].add(val ^ grid[0][c])
                
        # Process remaining rows
        for r in range(1, rows):
            # Update the first column of the current row
            new_col_0_set = set()
            for val in dp[0]:
                new_col_0_set.add(val ^ grid[r][0])
            dp[0] = new_col_0_set
            
            # Update the rest of the columns
            for c in range(1, cols):
                current_set = set()
                # From top cell
                for val in dp[c]:
                    current_set.add(val ^ grid[r][c])
                # From left cell
                for val in dp[c - 1]:
                    current_set.add(val ^ grid[r][c])
                dp[c] = current_set
                
        # The minimum possible XOR value at the bottom-right cell
        return min(dp[cols - 1])