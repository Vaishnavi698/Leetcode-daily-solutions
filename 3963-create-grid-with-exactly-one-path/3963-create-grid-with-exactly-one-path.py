from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        # Initialize the grid with obstacles '#'
        grid = [['#' ] * n for _ in range(m)]
        
        # Make the entire first row free
        for j in range(n):
            grid[0][j] = '.'
            
        # Make the entire last column free
        for i in range(m):
            grid[i][n - 1] = '.'
            
        return [''.join(row) for row in grid]