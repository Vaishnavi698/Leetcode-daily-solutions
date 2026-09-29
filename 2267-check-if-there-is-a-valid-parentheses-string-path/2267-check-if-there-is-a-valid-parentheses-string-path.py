from functools import lru_cache
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Necessary conditions
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        max_possible_balance = (m + n) // 2
        
        @lru_cache(None)
        def dfs(r: int, c: int, balance: int) -> bool:
            # Update balance for current cell
            balance += 1 if grid[r][c] == '(' else -1
            
            # Prune invalid paths
            if balance < 0 or balance > max_possible_balance:
                return False
            
            # Reached destination
            if r == m - 1 and c == n - 1:
                return balance == 0
            
            # Move Down
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
            
            # Move Right
            if c + 1 < n and dfs(r, c + 1, balance):
                return True
            
            return False
        
        return dfs(0, 0, 0)