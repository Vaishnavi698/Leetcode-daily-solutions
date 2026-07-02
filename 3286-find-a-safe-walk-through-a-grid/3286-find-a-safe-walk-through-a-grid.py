import collections

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        max_health_at = [[-1] * n for _ in range(m)]
        
       
        start_health = health - grid[0][0]
        
      
        if start_health <= 0:
            return False
            
        max_health_at[0][0] = start_health
        
      
        queue = collections.deque([(0, 0, start_health)])
        
      
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            r, c, h = queue.popleft()
            
          
            if r == m - 1 and c == n - 1 and h > 0:
                return True
                
         
            if h < max_health_at[r][c]:
                continue
                
          
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
              
                if 0 <= nr < m and 0 <= nc < n:
                   
                    next_health = h - grid[nr][nc]
                    
                   
                    if next_health > max_health_at[nr][nc]:
                        max_health_at[nr][nc] = next_health
                        
                       
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc, next_health))
                        else:
                            queue.append((nr, nc, next_health))
                            
      
        return False
        