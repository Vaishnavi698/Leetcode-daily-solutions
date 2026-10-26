from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r: int, c: int) -> int:
            # Out of bounds or water (0)
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
                
            # Get current value and mark as visited by sinking it to 0
            val = grid[r][c]
            grid[r][c] = 0
            
            # Recurse in all 4 directions and accumulate sum
            val += dfs(r + 1, c)
            val += dfs(r - 1, c)
            val += dfs(r, c + 1)
            val += dfs(r, c - 1)
            
            return val
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    # Found an island, compute its total value
                    island_sum = dfs(r, c)
                    if island_sum % k == 0:
                        count += 1
                        
        return count